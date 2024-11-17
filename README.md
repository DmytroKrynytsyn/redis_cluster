# **Redis Cluster, High Availability (HA) Architecture**
![redis_cluster](https://github.com/user-attachments/assets/53a70a68-282d-4449-8698-eef86f3bc3fe)

This project demonstrates the provisioning and configuration of a Redis cluster with one master and one read replica. It showcases a DevOps workflow integrating **Terraform**, **Terragrunt**, and **Ansible**, following best practices with modular and reusable Ansible roles.

The architecture is designed to meet **high availability (HA) requirements** for enterprise-grade solutions, ensuring reliability, fault tolerance, and scalability.

---

## **Project Highlights**
- **High Availability (HA) Architecture**:
  - Designed with **one master node** and **one read replica** to ensure continuity of operations in case of failure.
  - The read replica provides redundancy and supports load balancing for read-heavy workloads, reducing downtime risks.
- **Infrastructure as Code (IaC):**
  - Utilized **Terraform** and **Terragrunt** to define and provision cloud resources.
- **Configuration Management:**
  - Leveraged **Ansible** for automating Redis cluster setup.
  - Created reusable and modular Ansible roles for clean and scalable configurations.
- **Enterprise-Ready Design**:
  - Built to support critical applications where uptime and data reliability are essential.

---

## **Technologies Used**
1. **Terraform**: Provisioned infrastructure.
2. **Terragrunt**: Simplified Terraform workflows with DRY principles.
3. **Ansible**: Automated server configuration and application setup.
4. **Redis**: Open-source, in-memory key-value store for high-performance caching and data storage.

---

## **Features**
- **High Availability**:
  - Provisioned a primary Redis master with a synchronized read replica to minimize downtime and support failover.
  - Ensures reliable performance for mission-critical applications.
- **Automated Setup**: End-to-end automation of infrastructure provisioning and cluster configuration.
- **Modular Design**: Separate Ansible roles for enhanced reusability.

---

## **Enterprise High Availability Compliance**
This architecture adheres to enterprise-level high availability (HA) standards by:
- **Minimizing Single Points of Failure**: The master-replica configuration ensures redundancy, reducing the risk of service interruption.
- **Load Distribution**: Read operations can be routed to the replica, offloading the master and ensuring better performance under heavy load.
- **Automatic Failover Ready**: With minor extensions, tools like Redis Sentinel can be integrated to enable automatic failover in case the master node becomes unavailable.
- **Scalability**: Easily extendable to include more replicas or cluster-based configurations for larger systems.

This approach aligns with HA requirements often found in industries like finance, e-commerce, and technology where uptime and reliability are paramount.

---

## **How to Use**
### **Pre-Requisites**
- Install:
  - Terraform
  - Terragrunt
  - Ansible
- Configure your cloud provider credentials (e.g., AWS).

### **Setup Instructions**
1. Clone this repository:
   ```bash
   git clone https://github.com/DmytroKrynytsyn/redis_cluster.git
   cd redis_cluster```
2. Provision cloud resources
    ```
    terragrunt apply -auto-approve --terragrunt-working-dir ./terra
    ```
3. Configure the cluster
    ```
    ansible-playbook -i ansible/dynamic_inventory.py ansible/playbooks/main.yml
    ```
