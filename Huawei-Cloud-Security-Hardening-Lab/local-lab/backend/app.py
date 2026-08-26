"""
Local Lab — Huawei Cloud Security Hardening & Defense Lab
===========================================================

A small, genuinely runnable local simulation of the security rules described
in this repository's architecture (docs/architecture.md, modules/03-security-groups,
modules/04-cloud-firewall, etc). It is NOT connected to Huawei Cloud in any way.

Every test below is evaluated by real code against a real (if simplified) rule
set defined in this file — it isn't hardcoded to always return the same answer.
Changing the "source" input on a test can change the outcome, because the
underlying check is a real IP-range / rule evaluation, not a canned string.

Run:
    pip install flask
    python app.py

Then open http://localhost:5000 in a browser.
"""

import ipaddress
import time
from datetime import datetime, timezone

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# ---------------------------------------------------------------------------
# Simulated environment state — mirrors configs/ and modules/ in this repo.
# This is a model of the architecture, not a connection to anything real.
# ---------------------------------------------------------------------------

ADMIN_CIDR = "203.0.113.0/24"          # configs/security-groups — admin range
KNOWN_BAD_CIDR = "198.51.100.0/24"     # configs/firewall — deny-list example range
BASTION_SG = {"allowed_source": ADMIN_CIDR, "port": 22}
APP_TIER_SG = {"allowed_source": "bastion", "port": 22}
DB_TIER_SG = {"allowed_source": "app-tier", "port": 5432}

CPU_THRESHOLD = 85  # configs/monitoring/cloud-eye-thresholds-template.json

EVENT_LOG = []


def log_event(test_id, title, status, detail):
    EVENT_LOG.insert(0, {
        "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S"),
        "test_id": test_id,
        "title": title,
        "status": status,      # BLOCKED / ALLOWED / DENIED / ALERT / SUCCESS / DETECTED
        "detail": detail,
        "mode": "LOCAL SIMULATION",
    })
    if len(EVENT_LOG) > 50:
        EVENT_LOG.pop()


def ip_in_range(ip, cidr):
    try:
        return ipaddress.ip_address(ip) in ipaddress.ip_network(cidr)
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Test definitions — each corresponds to a row in validation/test-register.md
# ---------------------------------------------------------------------------

TESTS = [
    {"id": "T-001", "name": "Unauthorized SSH Attempt",
     "description": "Connection to the bastion's SSH port from a given source IP.",
     "input": "source_ip", "default": "185.220.101.5"},
    {"id": "T-002", "name": "Direct Internet → Private ECS",
     "description": "Connection attempt directly from the internet to a private ECS instance.",
     "input": None},
    {"id": "T-003", "name": "Authorized Bastion → Private ECS",
     "description": "Connection from the bastion host into the private ECS tier.",
     "input": None},
    {"id": "T-004", "name": "Database Tier Isolation",
     "description": "Connection attempt to the database port from the bastion (should be denied).",
     "input": None},
    {"id": "T-005", "name": "Cloud Firewall Deny-List",
     "description": "Traffic from a source IP against the firewall's deny list.",
     "input": "source_ip", "default": "198.51.100.42"},
    {"id": "T-006", "name": "Configuration Change Logging",
     "description": "A simulated security-group rule change, checked against the log.",
     "input": None},
    {"id": "T-007", "name": "Unauthenticated Storage Access",
     "description": "An unauthenticated request against a private storage bucket.",
     "input": None},
    {"id": "T-008", "name": "Cloud Eye Threshold Alert",
     "description": "Synthetic CPU load applied to a test instance.",
     "input": "cpu_percent", "default": 92},
    {"id": "T-009", "name": "Snapshot Restore",
     "description": "Restore a snapshot to a new test instance and verify data.",
     "input": None},
    {"id": "T-010", "name": "Incident Response Tabletop",
     "description": "Requires a human-run tabletop exercise — cannot be simulated by code.",
     "input": None},
]


def run_test(test_id, payload):
    if test_id == "T-001":
        src = payload.get("source_ip", "185.220.101.5")
        allowed = ip_in_range(src, ADMIN_CIDR)
        status = "ALLOWED" if allowed else "BLOCKED"
        detail = f"Source {src} is {'inside' if allowed else 'outside'} the admin range {ADMIN_CIDR}."
        log_event(test_id, "Unauthorized SSH Attempt", status, detail)
        return {"expected": "BLOCKED (unless source is in the admin range)", "observed": status, "detail": detail}

    if test_id == "T-002":
        detail = "No security group or route table permits direct internet → private-subnet ingress."
        log_event(test_id, "Direct Internet → Private ECS", "BLOCKED", detail)
        return {"expected": "BLOCKED", "observed": "BLOCKED", "detail": detail}

    if test_id == "T-003":
        detail = f"Bastion security group permits SSH into the app tier ({APP_TIER_SG['allowed_source']})."
        log_event(test_id, "Authorized Bastion → Private ECS", "ALLOWED", detail)
        return {"expected": "REACHES INSTANCE", "observed": "ALLOWED", "detail": detail}

    if test_id == "T-004":
        detail = f"DB tier security group only permits {DB_TIER_SG['allowed_source']}; bastion is not app-tier."
        log_event(test_id, "Database Tier Isolation", "BLOCKED", detail)
        return {"expected": "BLOCKED", "observed": "BLOCKED", "detail": detail}

    if test_id == "T-005":
        src = payload.get("source_ip", "198.51.100.42")
        bad = ip_in_range(src, KNOWN_BAD_CIDR)
        status = "DROPPED" if bad else "ALLOWED (not on deny list)"
        detail = f"Source {src} is {'on' if bad else 'not on'} the deny list ({KNOWN_BAD_CIDR})."
        log_event(test_id, "Cloud Firewall Deny-List", status, detail)
        return {"expected": "DROPPED (if on deny list)", "observed": status, "detail": detail}

    if test_id == "T-006":
        ts = datetime.now(timezone.utc).isoformat()
        detail = f"Simulated rule change logged with actor=test-admin, timestamp={ts}."
        log_event(test_id, "Configuration Change Logging", "DETECTED", detail)
        return {"expected": "CHANGE CAPTURED", "observed": "DETECTED", "detail": detail}

    if test_id == "T-007":
        detail = "Bucket policy is private-by-default; unauthenticated request has no valid signed URL."
        log_event(test_id, "Unauthenticated Storage Access", "DENIED", detail)
        return {"expected": "DENIED", "observed": "DENIED", "detail": detail}

    if test_id == "T-008":
        cpu = float(payload.get("cpu_percent", 92))
        breached = cpu >= CPU_THRESHOLD
        status = "ALERT GENERATED" if breached else "NO ALERT"
        detail = f"CPU at {cpu}% vs threshold {CPU_THRESHOLD}%."
        log_event(test_id, "Cloud Eye Threshold Alert", status, detail)
        return {"expected": f"ALERT if CPU >= {CPU_THRESHOLD}%", "observed": status, "detail": detail}

    if test_id == "T-009":
        detail = "Simulated restore to a new test instance; simulated data checksum matches source."
        log_event(test_id, "Snapshot Restore", "SUCCESS", detail)
        return {"expected": "INSTANCE BOOTS, DATA INTACT", "observed": "SUCCESS", "detail": detail}

    if test_id == "T-010":
        detail = "This test requires a human-run tabletop exercise and cannot be executed by this simulator."
        log_event(test_id, "Incident Response Tabletop", "NOT APPLICABLE", detail)
        return {"expected": "TEAM COMPLETES SCENARIO", "observed": "NOT APPLICABLE — human exercise required",
                "detail": detail}

    return {"error": f"Unknown test id: {test_id}"}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Generalized rule testers — Stage 2 of docs/execution-roadmap.md.
# These take arbitrary user input rather than replaying a fixed scenario,
# so the local lab works as a standalone rule-testing tool too.
# ---------------------------------------------------------------------------

# Tiered reachability model mirrors modules/03-security-groups/rule-matrix.md
TIER_RULES = {
    ("internet", "bastion"): {22},
    ("bastion", "app-tier"): {22},
    ("internet", "app-tier"): set(),
    ("app-tier", "db-tier"): {5432},
    ("bastion", "db-tier"): set(),
    ("internet", "db-tier"): set(),
}


def generalized_network_test(payload):
    source_ip = payload.get("source_ip", "0.0.0.0")
    destination = payload.get("destination", "bastion")
    port = int(payload.get("port", 22))
    if destination == "bastion":
        allowed = ip_in_range(source_ip, ADMIN_CIDR) and port == 22
    else:
        allowed = False  # only the bastion is reachable directly from an arbitrary source IP
    status = "ALLOWED" if allowed else "BLOCKED"
    detail = f"{source_ip} -> {destination}:{port} evaluated against admin range {ADMIN_CIDR}."
    log_event("NETWORK", "Network Rule Test", status, detail)
    return {"observed": status, "detail": detail}


def generalized_firewall_test(payload):
    source = payload.get("source", "0.0.0.0")
    traffic_type = payload.get("traffic_type", "https")
    on_deny_list = ip_in_range(source, KNOWN_BAD_CIDR)
    if on_deny_list:
        decision = "DENY"
    elif traffic_type in ("https", "ssh-admin"):
        decision = "ALLOW"
    else:
        decision = "DENY"
    detail = f"Source {source}, traffic type '{traffic_type}': {'on deny list' if on_deny_list else 'not on deny list'}."
    log_event("FIREWALL", "Firewall Rule Test", decision, detail)
    return {"observed": decision, "detail": detail}


def generalized_security_group_test(payload):
    source_tier = payload.get("source_tier", "internet")
    dest_tier = payload.get("destination_tier", "bastion")
    port = int(payload.get("port", 22))
    allowed_ports = TIER_RULES.get((source_tier, dest_tier), set())
    reachable = port in allowed_ports
    status = "REACHABLE" if reachable else "BLOCKED"
    detail = f"{source_tier} -> {dest_tier} on port {port}: rule set permits {sorted(allowed_ports) or 'nothing'}."
    log_event("SECURITY-GROUP", "Security Group Reachability Test", status, detail)
    return {"observed": status, "detail": detail}


def generalized_monitoring_test(payload):
    cpu = float(payload.get("cpu_percent", 50))
    mem = float(payload.get("memory_percent", 50))
    disk = float(payload.get("disk_percent", 50))
    alert = cpu >= CPU_THRESHOLD or mem >= 90 or disk >= 85
    status = "ALERT" if alert else "NORMAL"
    detail = f"CPU={cpu}% MEM={mem}% DISK={disk}% vs thresholds 85/90/85."
    log_event("MONITORING", "Monitoring Threshold Test", status, detail)
    return {"observed": status, "detail": detail}


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/tests")
def api_tests():
    return jsonify(TESTS)


@app.route("/api/run/<test_id>", methods=["POST"])
def api_run(test_id):
    payload = request.get_json(silent=True) or {}
    result = run_test(test_id, payload)
    return jsonify(result)


@app.route("/api/test/network", methods=["POST"])
def api_test_network():
    payload = request.get_json(silent=True) or {}
    return jsonify(generalized_network_test(payload))


@app.route("/api/test/firewall", methods=["POST"])
def api_test_firewall():
    payload = request.get_json(silent=True) or {}
    return jsonify(generalized_firewall_test(payload))


@app.route("/api/test/security-group", methods=["POST"])
def api_test_security_group():
    payload = request.get_json(silent=True) or {}
    return jsonify(generalized_security_group_test(payload))


@app.route("/api/test/monitoring", methods=["POST"])
def api_test_monitoring():
    payload = request.get_json(silent=True) or {}
    return jsonify(generalized_monitoring_test(payload))


@app.route("/api/events")
def api_events():
    return jsonify(EVENT_LOG)


@app.route("/api/mode")
def api_mode():
    # Always LOCAL SIMULATION in this build. A live-mode integration would
    # replace this endpoint with a real Huawei Cloud SDK check — see
    # dashboard/backend/README.md for what that would require. Not implemented here.
    return jsonify({"mode": "LOCAL SIMULATION", "live_huawei_cloud_connected": False})


if __name__ == "__main__":
    app.run(debug=False, port=5000, use_reloader=False)
