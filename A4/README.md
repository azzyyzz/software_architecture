# Video Processing Pipeline (Pipes and Filters Pattern)

This project implements a **video processing pipeline** using the **Pipes and Filters** architectural pattern. The pipeline applies a series of filters (such as black-and-white conversion, flipping, cropping, and resizing) to video frames in sequence.

## Features
- **Modular filters**: Each filter is implemented as a separate class, making it easy to add, remove, or modify filters.
- **Pipes and Filters architecture**: Data (video frames) flows through a pipeline of filters, where each filter processes the frame and passes it along.
- **Extensibility**: Easily extend the pipeline by adding new filters without modifying the core logic.

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/): For video processing.

You can install OpenCV using pip:
```bash
pip install opencv-python
