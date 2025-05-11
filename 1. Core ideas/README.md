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
<img width="644" alt="Screenshot 2025-03-22 at 12 02 31" src="https://github.com/user-attachments/assets/e09a7965-ecc1-46f3-99e0-80832cefd2f1" />


2. **Run the Installation Wizard**: The installer will guide you through the necessary steps to install VirtualBox on your system. Follow the prompts in the installation wizard.

<img width="614" alt="Screenshot 2025-03-22 at 12 03 31" src="https://github.com/user-attachments/assets/f2c2c2c1-484d-42b4-9571-4df2ed93d94b" />

3. **Completing the Installation**: Once the installation is complete, you will see a confirmation screen indicating that VirtualBox has been successfully installed.
<img width="638" alt="Screenshot 2025-03-22 at 12 04 09" src="https://github.com/user-attachments/assets/528d9ffa-ce33-489c-862d-29d20fbdf077" />

4. **Launch VirtualBox**: Open the `Applications` folder and double-click on the VirtualBox icon to run it. When you launch VirtualBox for the first time, you might be prompted to choose between `Basic` and `Expert` modes, depending on your preference and experience level.
<img width="691" alt="Screenshot 2025-03-22 at 12 06 14" src="https://github.com/user-attachments/assets/eba3a0e4-2307-4917-9c72-e1f6ccf5f5df" />

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

<img width="938" alt="Screenshot 2025-03-22 at 14 02 11" src="https://github.com/user-attachments/assets/d3b97238-cbb4-49b3-acb6-c605fef0c8ae" />
<img width="944" alt="Screenshot 2025-03-22 at 14 02 33" src="https://github.com/user-attachments/assets/38495130-c963-4034-b774-2e79857a935c" />
<img width="948" alt="Screenshot 2025-03-22 at 14 02 46" src="https://github.com/user-attachments/assets/66747441-d8cf-4d14-aef2-c2b94089ff8d" />
<img width="944" alt="Screenshot 2025-03-22 at 14 02 51" src="https://github.com/user-attachments/assets/0f0ed82e-fa5a-4c6d-802e-81284f1c6ace" />
<img width="981" alt="Screenshot 2025-03-23 at 14 51 10" src="https://github.com/user-attachments/assets/301da6e9-54d7-44f7-addc-b1d47199060f" />

After successfully installing Ubuntu, follow these steps to start using your system.

### 1. Starting Ubuntu

Start VirtualBox and select your Ubuntu virtual machine.  Click on the "Start" button to boot into Ubuntu.

<img width="977" alt="Screenshot 2025-03-23 at 15 04 01" src="https://github.com/user-attachments/assets/8f762f8b-48c9-45c8-bd80-c521ff82d7f9" />

### 2. Booting from the Installation Media

When you start your virtual machine, you will first see the GNU GRUB screen. From here, select "Try or Install Ubuntu Server" to proceed with the installation.

<img width="694" alt="Screenshot 2025-03-22 at 14 05 45" src="https://github.com/user-attachments/assets/714a9014-030f-47dd-85c9-675ea022e7cb" />

### 3. Configuring Your User Profile

During the installation process, you'll be asked to create a user account. This account will be used for logging into the Ubuntu system. You'll need to provide:
  - Your full name
  - Your desired username
  - A strong password and confirm it
<img width="865" alt="Screenshot 2025-03-22 at 14 32 37" src="https://github.com/user-attachments/assets/79bde00e-3e39-49e8-801a-8720bb6117d0" />

  It's recommended to have the same name and username. 

### 4. Installation System
After that, you need to wait for the system to complete the installation and updates, then reboot it.

<img width="862" alt="Screenshot 2025-03-22 at 14 32 54" src="https://github.com/user-attachments/assets/ed092f20-b55c-4711-a6eb-2b44acc2f687" />
<img width="860" alt="Screenshot 2025-03-22 at 14 36 32" src="https://github.com/user-attachments/assets/6f8f9896-f8bd-4b9c-a94e-634f94975659" />

### 5. Log into Ubuntu
At the login screen, enter the username and password you created during the installation process.

<img width="1040" alt="Screenshot 2025-03-23 at 15 29 03" src="https://github.com/user-attachments/assets/ee08b673-5a84-4242-9fe0-16714ab82a60" />

### 6. Exploring the Ubuntu Desktop
Once logged in, you'll be presented with the Ubuntu Desktop environment. You can begin exploring or installing additional software as needed.

<img width="1051" alt="Screenshot 2025-03-23 at 00 04 26" src="https://github.com/user-attachments/assets/8a296712-6f07-4005-b6a6-a6b4c538acdb" />

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
<img width="403" alt="Screenshot 2025-03-23 at 15 30 18" src="https://github.com/user-attachments/assets/a8149e64-a4aa-4fe9-8a57-a3c8a8505afb" />

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

