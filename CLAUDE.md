# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Manim animations project for creating mathematical/educational videos using the Manim Community library.

## Commands

```bash
# Install dependencies
uv sync

# Render a scene (outputs to media/videos/)
uv run manim -pql main.py SceneName

# Render flags:
#   -p  Preview after rendering
#   -ql Low quality (480p, 15fps) - fast for development
#   -qm Medium quality (720p, 30fps)
#   -qh High quality (1080p, 60fps)
#   -qk 4K quality (2160p, 60fps)

# Render specific scene with custom output
uv run manim -qm -o output_name.mp4 main.py SceneName
```

## Architecture

- **Scene classes**: Each animation is a class inheriting from `Scene` with a `construct()` method
- **media/**: Output directory for rendered content (videos/, images/, Tex/)

## Manim Patterns

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Create objects
        circle = Circle()
        # Animate
        self.play(Create(circle))
        self.wait()
```

## Additional Examples

Many examples can be found here: https://docs.manim.community/en/stable/examples.html
