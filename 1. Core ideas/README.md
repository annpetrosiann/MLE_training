# Installation Guide

This guide provides step-by-step instructions on setting up a Linux environment using VirtualBox, installing Ubuntu as the operating system, and configuring Docker to run containers. Each section is designed to help through the installation and setup process, ensuring a smooth and successful development environment setup.

## 1. VirtualBox

VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use. It is an open-source software that lets you run multiple operating systems simultaneously. This section will guide you through the process of downloading and installing VirtualBox on your current operating system.

### Steps

- Download VirtualBox from the [official website](https://www.virtualbox.org/wiki/Downloads).
- Follow the installation instructions for your operating system.
- For Macs with chips starting from the M1, install VirtualBox for Apple Silicon hosts.


After downloading the installer, follow these steps to install VirtualBox:

1. **Launch the Installer**: Double-click on the `VirtualBox.pkg` file to start the installation process.
<img width="644" alt="Screenshot 2025-03-22 at 12 02 31" src="https://github.com/user-attachments/assets/60719658-2d7d-4b89-ad0f-c18f97ad97c2" />


2. **Run the Installation Wizard**: The installer will guide you through the necessary steps to install VirtualBox on your system. Follow the prompts in the installation wizard.

<img width="614" alt="Screenshot 2025-03-22 at 12 03 31" src="https://github.com/user-attachments/assets/0a6d376c-502d-4709-83f0-2997f56f56ac" />

3. **Completing the Installation**: Once the installation is complete, you will see a confirmation screen indicating that VirtualBox has been successfully installed.

<img width="638" alt="Screenshot 2025-03-22 at 12 04 09" src="https://github.com/user-attachments/assets/85c677ac-06a0-40df-8131-d8f8c2518945" />

4. **Launch VirtualBox**: Open the `Applications` folder and double-click on the VirtualBox icon to run it. When you launch VirtualBox for the first time, you might be prompted to choose between `Basic` and `Expert` modes, depending on your preference and experience level.

<img width="691" alt="Screenshot 2025-03-22 at 12 06 14" src="https://github.com/user-attachments/assets/354eba7f-1089-4159-8966-6820eca1e725" />

Now that you have VirtualBox installed, you can proceed to create and manage your virtual machines. 
## 2. Ubuntu

Ubuntu is a popular Linux distribution based on Debian. It is mostly composed of free and open-source software and is recommended for beginners due to its ease of use and installation. This part will cover how to set up Ubuntu inside VirtualBox.

### Types
- **Ubuntu Desktop** is intended for general use on personal computers and laptops. It comes with a graphical user interface (GUI), making it user-friendly for everyday tasks, and includes standard software like web browsers, office suites, and media players.

- **Ubuntu Server** is designed for server use, catering to infrastructure and enterprise needs. It operates without a GUI by default and is managed via the command line for efficiency and reduced resource usage. It's optimized for network services such as web hosting, file servers, and database management.

- **Ubuntu Server for ARM** is similar to Ubuntu Server but optimized for the ARM architecture. It is ideal for ARM-based servers, commonly used in energy-efficient and space-constrained environments, and supports a variety of ARM hardware, ensuring compatibility and performance in specialized setups.
### Steps

**1. Download Ubuntu**: Download the Ubuntu ISO from [Ubuntu's official page](https://ubuntu.com/download/server/arm).

**2. Create a New Virtual Machine**: Open VirtualBox and click "New" to create a new VM.  
**3. Install Ubuntu**: Set the name as "Ubuntu" and adjust the memory and disk settings according to your preference.  Attach the downloaded ISO file to the VM and follow the installation prompts.
Once installation is complete, you can start using Ubuntu within VirtualBox.

<img width="938" alt="Screenshot 2025-03-22 at 14 02 11" src="https://github.com/user-attachments/assets/35b445c9-b7bd-4f19-bb81-91cbba58fd67" />
<img width="944" alt="Screenshot 2025-03-22 at 14 02 33" src="https://github.com/user-attachments/assets/a9f1620a-5604-4dba-aa3a-0292e44d9af0" />
<img width="948" alt="Screenshot 2025-03-22 at 14 02 46" src="https://github.com/user-attachments/assets/01358634-9edd-47fb-8368-e97f23d31836" />
<img width="944" alt="Screenshot 2025-03-22 at 14 02 51" src="https://github.com/user-attachments/assets/e7819a8a-0c41-4194-9021-2682c2d167f4" />
<img width="981" alt="Screenshot 2025-03-23 at 14 51 10" src="https://github.com/user-attachments/assets/5a4c2dae-8e93-4702-a77d-a4251b28a137" />


After successfully installing Ubuntu, follow these steps to start using your system.

### 1. Starting Ubuntu

Start VirtualBox and select your Ubuntu virtual machine.  Click on the "Start" button to boot into Ubuntu.

<img width="977" alt="Screenshot 2025-03-23 at 15 04 01" src="https://github.com/user-attachments/assets/4ccacb94-fdaf-4d47-8c46-58a627bf9c99" />

### 2. Booting from the Installation Media

When you start your virtual machine, you will first see the GNU GRUB screen. From here, select "Try or Install Ubuntu Server" to proceed with the installation.

<img width="694" alt="Screenshot 2025-03-22 at 14 05 45" src="https://github.com/user-attachments/assets/2bc7c195-3f79-4cde-a019-c374bae4a5f9" />

### 3. Configuring Your User Profile

During the installation process, you'll be asked to create a user account. This account will be used for logging into the Ubuntu system. You'll need to provide:
  - Your full name
  - Your desired username
  - A strong password and confirm it
<img width="865" alt="Screenshot 2025-03-22 at 14 32 37" src="https://github.com/user-attachments/assets/0eabbe99-9591-4e68-8ab2-b21f0a4c8f45" />

  It's recommended to have the same name and username. 

### 4. Installation System
After that, you need to wait for the system to complete the installation and updates, then reboot it.

<img width="862" alt="Screenshot 2025-03-22 at 14 32 54" src="https://github.com/user-attachments/assets/928d67fd-0ec2-4669-9139-b2c75f1ba89c" />
<img width="860" alt="Screenshot 2025-03-22 at 14 36 32" src="https://github.com/user-attachments/assets/74f7929b-e869-4a98-8028-b0bfa7efc321" />


### 5. Log into Ubuntu
At the login screen, enter the username and password you created during the installation process.

<img width="1040" alt="Screenshot 2025-03-23 at 15 29 03" src="https://github.com/user-attachments/assets/761a0c70-9360-460d-9c85-4de59f1e3784" />

### 6. Exploring the Ubuntu Desktop
Once logged in, you'll be presented with the Ubuntu Desktop environment. You can begin exploring or installing additional software as needed.

<img width="1051" alt="Screenshot 2025-03-23 at 00 04 26" src="https://github.com/user-attachments/assets/5400eb21-b0cf-48dd-ae8d-4e6e8e5b259b" />

### Updating and Upgrading

It's important to update the  system. Open a terminal and enter the [following commands](https://www.youtube.com/watch?v=LjL_N0OZxvY) to update and upgrade  packages:
  ```bash
    sudo apt update
    sudo apt upgrade
    sudo apt install tasksel
    sudo apt install ubuntu-desktop
    sudo reboot now
```
## 4. Docker

Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers. This section explains how to install Docker and Docker Compose on Ubuntu running in VirtualBox, enabling you to manage applications in a lightweight and modular fashion.

### Steps

1. First, make sure your package list is up to date,
2. If Docker is not already installed on your system, you can install it using the following command:

  ```bash
    sudo apt install docker.io
  ```
3. To install Docker Compose, you can use the below commands. You may need to download the latest version of Docker Compose from the official GitHub repository:

```bash
  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

  sudo chmod +x /usr/local/bin/docker-compose
```
4. Check if Docker Compose was installed successfully by running,
```bash
     sudo docker-compose --version
```

To manage **Docker without having to prepend sudo to every command**, you can add your user to the Docker group. This allows your user to execute Docker commands without needing superuser privileges. Here's how you can do it:

- Create the Docker group if it doesn't already exist:

```bash
   sudo groupadd docker
```
- Add your user to the Docker group:
```bash
  sudo usermod -aG docker $USER
```
- You can either log out and log back in, or use the following command to refresh the group membership in the current session:
 ```bash
   newgrp docker
```
- Verify that you can run Docker commands without sudo:
```bash
  docker run hello-world
```

This command should run without any issues and without requiring sudo.

