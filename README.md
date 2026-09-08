# Enterprise Log Rotation & Cleanup Automation

A robust, stateless Python utility designed for DevSecOps environments to prevent disk exhaustion and optimize EBS volume costs on cloud infrastructure (e.g., AWS EC2).

## Operational Values
Unmanaged application logs and temporary files can quickly consume 100% of available storage, causing critical server crashes. This script automates lifecycle management, ensuring compliance and system stability without manual SSH intervention.

## Features
* **Time-Based Purging:** Calculates accurate file age via Epoch time to securely delete files older than a dynamic threshold.
* **Resilience & Edge Cases:** Includes strict error handling for `PermissionError` and missing directories to prevent automated pipeline crashes.
* **Audit Compliance:** Generates dual-stream logs (stdout and permanent file) for a verifiable trail of all purged assets.
* **CLI Integration:** Built with `argparse` for seamless integration into Linux Cron jobs and CI/CD workflows.

## Usage
Execute the script from the terminal, passing your target directory and retention policy as arguments:

```bash
python3 log_rotator.py -d /var/log/myapp -r 30