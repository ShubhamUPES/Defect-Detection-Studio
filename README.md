```markdown
# Defect Detection Studio

A desktop application for training and deploying AI-powered visual defect detection systems on industrial production lines. Built with PyQt6 and SQLAlchemy.

---

## Features

- **Project Management** — Create and manage multiple inspection projects (Object Detection or Instance Segmentation)
- **Image Upload & Dataset Management** — Upload images, manage splits (Train/Valid/Test), search and filter
- **Annotation Tools** — BBox, Polygon, Count, Tracking, ROI tools with label assignment on an interactive canvas
- **Dataset Versioning** — Freeze working datasets into versioned snapshots with augmentation and preprocessing config
- **Model Training** — Configure hyperparameters (epochs, batch size, image size, learning rate) and train from any dataset version
- **Model Registry** — Compare mAP, Precision, Recall, and Latency across model versions; promote to Production
- **Inference Testing** — Upload a test image and run simulated inference with confidence scores
- **Class & Tag Management** — Add, rename, and delete annotation classes across the project
- **PLC / Communication Settings** — Configure EtherNet/IP and other protocol settings
- **Activity Log** — Full audit trail of versions, training runs, and system events

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | PyQt6 |
| Database | SQLite via SQLAlchemy 2.0 |
| Auth | bcrypt password hashing |
| Image handling | Pillow, QPixmap |
| ML (future) | PyTorch, ONNX, TensorRT |

---

## Project Structure

```
inspectx-python/
├── main.py                         # Entry point
├── requirements.txt
├── assets/
│   └── logo.jpg           # Company logo
└── app/
    ├── database/
    │   ├── engine.py               # SQLAlchemy engine + session
    │   └── models.py               # User, Project, Image, Annotation, Version, MLModel, Log
    ├── services/
    │   ├── auth_service.py
    │   ├── project_service.py
    │   ├── image_service.py
    │   ├── annotation_service.py
    │   ├── version_service.py
    │   └── model_service.py
    └── ui/
        ├── theme.py                # Design tokens and color palette
        ├── state.py                # Central AppState (PyQt signals + service calls)
        ├── main_window.py          # Top-level window and routing
        ├── pages/
        │   ├── login_page.py
        │   ├── home_page.py
        │   ├── overview_page.py
        │   ├── annotate_page.py
        │   ├── dataset_page.py
        │   ├── versions_page.py
        │   ├── classes_page.py
        │   ├── train_page.py
        │   ├── models_page.py
        │   ├── test_page.py
        │   └── settings_page.py
        └── widgets/
            ├── annotation_canvas.py
            ├── sidebar.py
            ├── topbar.py
            ├── card.py
            ├── badge.py
            ├── metric_card.py
            ├── image_card.py
            └── toast.py
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone <your-repo-url>
cd inspectx-python
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

### Default Credentials

| Account | Username | Password |
|---|---|---|
| Admin | `admin` | `admin` |
| Demo | `demo@inspectx.ai` | `demo1234` |

New accounts are auto-registered on first login.

---

## Workflow

```
Upload Images → Annotate → Generate Dataset Version → Train Model → Test → Deploy
```

1. Create a project (Detection or Segmentation)
2. Upload images via drag & drop or file picker
3. Annotate with BBox or Polygon tools, assign class labels
4. Generate a versioned dataset snapshot
5. Train a model with configurable hyperparameters
6. Review metrics (mAP, Precision, Recall, Latency)
7. Promote the best model to Production
8. Run inference tests on new images

---

## Data Storage

All project data is stored locally:

- **Database:** `app/database/inspectx.db` (SQLite)
- **Images:** `~/.inspectx/projects/<project_id>/images/`

---


```
