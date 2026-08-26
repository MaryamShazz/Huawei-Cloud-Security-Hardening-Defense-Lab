# Implementation Detail — VPC Network Security

1. Create the VPC with a defined CIDR block.
2. Create a public subnet and a private subnet within it, each with its own CIDR range carved from the VPC block.
3. Attach an Internet Gateway to the VPC and associate it only with the public subnet's route table.
4. Create a NAT gateway in the public subnet and point the private subnet's route table at it for outbound-only access.
5. Review the private subnet's route table directly to confirm there's no route to the Internet Gateway.

Reference: `subnet-plan.md` and `route-review.md` in this folder.
