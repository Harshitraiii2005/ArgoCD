
# 🚀 ArgoCD Tutorial

[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)  
[![GitHub Repo](https://img.shields.io/badge/github-repo-black)](https://github.com/Harshitraiii2005/ArgoCD)  
[![Kubernetes](https://img.shields.io/badge/kubernetes-%E2%9C%93-blue)](https://kubernetes.io/)  
[![ArgoCD](https://img.shields.io/badge/argocd-%E2%9C%93-red)](https://argo-cd.readthedocs.io/)

> Hands-on tutorial repository to learn **ArgoCD**, a GitOps continuous delivery tool for Kubernetes.  
> Includes examples of declarative app deployment, syncing manifests, and automating updates from Git.

---

## 🌟 What is ArgoCD?

**ArgoCD** is a **GitOps continuous delivery tool** that automatically deploys applications to Kubernetes clusters from Git repositories.  
It ensures that your cluster state always **matches the desired state defined in Git** and provides **monitoring, versioning, and rollback** capabilities.

---

## 💡 Why Use ArgoCD?

- **Declarative deployment:** Kubernetes manifests, Helm charts, or Kustomize stored in Git  
- **GitOps workflow:** Git is the single source of truth for app configuration  
- **Automatic sync:** Detect changes in Git and automatically update your cluster  
- **Rollback & history:** Track revisions and rollback to previous versions easily  
- **Integration:** Works with existing CI/CD tools like Jenkins, GitHub Actions, and Argo Workflows  

---

## ⚡ Key Concepts

1. **Application** – The main unit ArgoCD manages; defines source repo, destination cluster, and path.  
2. **Sync** – Operation to bring the cluster state in line with Git.  
3. **Deployment** – Automatic application rollout from Git manifests.  
4. **Health & Status** – Monitor deployed apps’ health and resource status through ArgoCD UI or CLI.  

---

## 🛠 Features

- Declarative app deployment via Git  
- Real-time cluster state monitoring  
- Automatic or manual sync strategies  
- Rollback to previous versions  
- Multi-cluster deployment support  

---

## 📦 Installation

Install ArgoCD CLI:

```bash
# MacOS
brew install argocd

# Linux
sudo curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo chmod +x /usr/local/bin/argocd
````

Install ArgoCD on Kubernetes cluster:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

---

## 🚀 How to Run

1. **Access ArgoCD UI**

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open `https://localhost:8080` in your browser.

2. **Login via CLI**

```bash
argocd login <ARGOCD_SERVER> --username admin --password <PASSWORD>
```

3. **Create and Sync Application**

```bash
argocd app create my-app \
    --repo https://github.com/Harshitraiii2005/ArgoCD.git \
    --path k8s/ \
    --dest-server https://kubernetes.default.svc \
    --dest-namespace default

argocd app sync my-app
```

---

## 📁 Repository Structure

```
.
├                 
├── deployment.yaml
│── application.yaml
├── README.md            # Project documentation          
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

* [ArgoCD Official Docs](https://argo-cd.readthedocs.io/)
* [Kubernetes](https://kubernetes.io/)
* GitOps principles and best practices

```

```
