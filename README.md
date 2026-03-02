# Manimations

**Claude-Assisted Visualizations with Manim**

Create professional animated data visualizations using natural language prompts. This project combines [Manim](https://www.manim.community/) (the mathematical animation library) with [Claude Code](https://claude.ai/code) to let you generate animated charts and graphics just by describing what you want.

## What is this project?

Manimations is a toolkit for creating animated data visualizations without needing to write code yourself. Using Claude Code (Anthropic's AI coding assistant), you can describe the animation you want in plain English, and Claude will generate the Manim code for you.

**Example outputs include:**
- Animated bar charts comparing business metrics
- Line charts showing data trends over time with "racing" animations
- Radar/spider charts for multi-dimensional comparisons
- Any mathematical or data visualization you can imagine

The animations render as MP4 videos that you can use in presentations, social media, or educational content.

## Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) (modern Python package manager)
- [Claude Code](https://claude.ai/code) CLI installed

### Setup

1. Clone or download this repository

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Verify the installation by rendering a test scene:
   ```bash
   uv run manim -pql animations/powertrade_radar.py RadarChartScene
   ```

## Usage

### Basic Commands

Make sure to use the good options for you:
* `-p` opens a preview right after rendering, very handy
* `-qX` selects the quality for rendering (use `-qh` for publishing), see below

```bash
# Render a scene (low quality, fast preview)
uv run manim -pql animations/your_scene.py SceneName

# Render in high quality (1080p, 60fps)
uv run manim -pqh animations/your_scene.py SceneName

# Quality options:
#   -ql  Low quality (480p, 15fps) - fast for development
#   -qm  Medium quality (720p, 30fps)
#   -qh  High quality (1080p, 60fps)
#   -qk  4K quality (2160p, 60fps)
#
# The -p flag opens a preview after rendering
```

Videos are saved to the `media/videos/` folder.

### Existing Animations

| Scene | File | Description |
|-------|------|-------------|
| `BarChartScene` | `powertrade_barchart.py` | Animated grouped bar chart comparing two brands across websites |
| `PowerTradeScene` | `powertrade_country.py` | Line chart "race" showing brand visibility over time by country |
| `RadarChartScene` | `powertrade_radar.py` | Spider/radar chart comparing brand performance across categories |

---

## Creating Animations with Claude Code

The real power of this project is using Claude Code to generate new animations from natural language descriptions. Here are example prompts you can use:

### Example 1: Simple Pie Chart

Open Claude Code in this directory and type:

```
Create a new animation file animations/sales_pie.py with an animated pie chart
showing quarterly sales: Q1: 35%, Q2: 25%, Q3: 22%, Q4: 18%.
Use a color scheme of blues and greens. Animate each slice appearing one by one
with a satisfying "pop" effect.
```

### Example 2: Animated Line Graph with Multiple Series

```
Create an animation called animations/stock_comparison.py that shows a line chart
comparing three tech stocks over 12 months. Use realistic-looking data with some
volatility. The lines should "draw" themselves from left to right simultaneously.
Add a legend and label each stock with its ticker symbol at the end of its line.
```

### Example 3: Horizontal Bar Chart Race

```
Make a "bar chart race" animation in animations/country_gdp.py showing the top 5
countries by GDP changing over 10 years. The bars should smoothly animate their
lengths and positions as rankings change. Include country flags next to each bar
if possible, otherwise use country codes.
```

### Example 4: Mathematical Visualization

```
Create an educational animation in animations/pythagorean.py that visually proves
the Pythagorean theorem. Start with a right triangle, then show squares being
constructed on each side, and finally demonstrate that a^2 + b^2 = c^2 by
animating the areas. Use clear colors and add LaTeX labels for the formula.
```

### Tips for Better Results

1. **Be specific** about colors, timing, and animation style
2. **Reference existing files** in the `animations/` folder for style consistency
3. **Iterate** - ask Claude to adjust timing, colors, or effects after seeing the first render
4. **Ask Claude to render** for you with the appropriate quality flag

Example follow-up prompts:
```
Render the scene in low quality so I can preview it

Make the animation 2 seconds longer with a slower fade-in

Change the color scheme to match our brand colors: #1E88E5 and #43A047
```

---

## Project Structure

```
manimations/
├── animations/          # Your Manim scene files
│   ├── powertrade_barchart.py
│   ├── powertrade_country.py
│   └── powertrade_radar.py
├── assets/              # Image assets (country flags, logos)
├── media/               # Rendered output (videos, images)
│   └── videos/
├── pyproject.toml       # Project dependencies
├── CLAUDE.md            # Instructions for Claude Code
└── README.md
```

## Learn More

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Examples Gallery](https://docs.manim.community/en/stable/examples.html)
- [Claude Code](https://claude.ai/code)

## License

MIT
