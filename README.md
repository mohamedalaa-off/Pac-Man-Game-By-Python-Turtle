<div align="center">

# 🕹️ Pac-Man: Python Turtle Edition

**A high-performance, classic arcade recreation built entirely with Python's standard libraries.**

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Library](https://img.shields.io/badge/Library-Turtle-orange?logo=python&logoColor=white)]()
[![Course](https://img.shields.io/badge/Course-Computer_Graphics-success?logo=codecademy&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat)](#-contributing)

[Explore the Code](#-technical-architecture) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## 📖 About The Project

> *"Rebuilding a classic, one frame at a time."*

This project is a meticulous recreation of the classic arcade game **Pac-Man**, developed completely in Python using the `turtle` graphics library. Originally conceived as a capstone project for a **Computer Graphics** course, this repository showcases fundamental game development concepts including rendering loops, coordinate-based collision detection, and entity state management—all without the overhead of heavy game engines like Pygame.

Whether you're a student learning Python, a nostalgic gamer, or an open-source contributor, this project provides a clean, well-documented codebase to explore.

### ✨ Key Features

* **🏎️ Optimized Game Loop:** Smooth frame rendering and entity updates using `turtle.tracer(0)` for immediate drawing.
* **👻 Autonomous Ghost AI:** Programmed enemy behaviors that hunt the player across the maze.
* **💥 Precise Collision Detection:** Custom coordinate mapping to handle walls, pellet consumption, and ghost encounters.
* **🏆 Dynamic Scoring & UI:** Real-time on-screen score updates and power-up tracking.
* **🪶 Zero Dependencies:** Runs right out of the box on any machine with Python installed. No `pip install` required.

---

## 🧠 Technical Architecture

This project is an excellent study in fundamental game design. Here's how it works under the hood:

* **Rendering Engine:** Utilizes Python's `turtle` module. Instead of standard slow turtle drawing, we manipulate the screen updates manually for instant frame rendering.
* **Grid-Based Movement:** The game board is mapped to a Cartesian coordinate system. Entity movements are snapped to a logical grid to ensure precise wall collisions.
* **State Management:** The game loop continuously checks states (e.g., `is_powered_up`, `is_game_over`) to alter Ghost behavior and Pac-Man's capabilities on the fly.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the game up and running on your local machine.

### Prerequisites

* Python 3.8 or higher.
* *Note: The `turtle` library comes pre-installed with standard Python distributions.*

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/mohamedalaa-off/Pac-Man-Game-By-Python-Turtle.git
   ```
2. **Navigate into the directory**
   ```sh
   cd Pac-Man-Game-By-Python-Turtle
   ```
3. **Launch the game**
   ```sh
   python main.py
   ```
   *(Ensure you run the correct entry-point script if it is named differently)*

---

## 🎮 Controls

Master the maze with simple, responsive controls:

| Key Binding | Action |
| :---: | :--- |
| <kbd>W</kbd> or <kbd>↑</kbd> | Move Up |
| <kbd>S</kbd> or <kbd>↓</kbd> | Move Down |
| <kbd>A</kbd> or <kbd>←</kbd> | Move Left |
| <kbd>D</kbd> or <kbd>→</kbd> | Move Right |
| <kbd>Esc</kbd> | Quit Game |

---

## 🗺️ Roadmap

We are always looking to improve the game. Current planned features include:

- [ ] Add retro arcade sound effects (`winsound` or `os` modules).
- [ ] Implement different AI personalities for each ghost (Blinky, Pinky, Inky, Clyde).
- [ ] Create multiple maze levels with increasing difficulty.
- [ ] Add a high-score tracker saved to a local `.txt` or `.json` file.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🛡️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <b>Built with ❤️ by <a href="https://github.com/mohamedalaa-off">mohamedalaa-off</a></b>
</div>
