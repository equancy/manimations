from manim import *
import random
import os


# Original Prompt:
# write a script powertrade_country.py to generate a scene with 5 time series as straight lines running from left to right
# in parallel as if they were racing.
# The series are tagged DE, ES, FR, IT, NL. Use vivid colors for these series.
# The x axis has 10 ticks from W11 to W21 evenly spaced (these are weeks).
# The y axis has 4 ticks with thin grey horizontal lines at 2K, 4K, 6K, 8K (thousands).
# Generate fake data for each series: one data point for each tick (week) for each serie, ranging from 2000 to 7000.
 
 
# Set seed for reproducibility
random.seed(42)

# Generate fake data for each series (10 weeks, values between 2000-7000)
# SERIES_DATA = {
#     "DE": [random.randint(2000, 7000) for _ in range(10)],
#     "ES": [random.randint(2000, 7000) for _ in range(10)],
#     "FR": [random.randint(2000, 7000) for _ in range(10)],
#     "IT": [random.randint(2000, 7000) for _ in range(10)],
#     "NL": [random.randint(2000, 7000) for _ in range(10)],
# }

# These are the real data extracted from the original graph
SERIES_DATA = {
    "DE": [1800, 1700, 100, 1075, 1100, 4300, 2000, 1500, 1500, 1400],
    "ES": [5400, 5300, 4600, 7434, 7200, 7400, 4700, 5200, 6300, 5800],
    "FR": [200, 300, 400, 640, 2000, 1800, 2600, 3400, 1400, 700],
    "IT": [2400, 2400, 2900, 3170, 2000, 3300, 3000, 3100, 1500, 2800],
    "NL": [1500, 0, 0, 1600, 0, 100, 200, 500, 0, 0],
}

# Vivid colors for each series
SERIES_COLORS = {
    "DE": "#FF3366",  # Vivid pink-red
    "ES": "#FFCC00",  # Vivid yellow
    "FR": "#00AAFF",  # Vivid blue
    "IT": "#00FF88",  # Vivid green
    "NL": "#FF6600",  # Vivid orange
}

# Flag image files (relative to script location)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FLAGS_DIR = os.path.join(SCRIPT_DIR, "..", "assets")
SERIES_FLAGS = {
    "DE": os.path.join(FLAGS_DIR, "de.png"),
    "ES": os.path.join(FLAGS_DIR, "es.png"),
    "FR": os.path.join(FLAGS_DIR, "fr.png"),
    "IT": os.path.join(FLAGS_DIR, "it.png"),
    "NL": os.path.join(FLAGS_DIR, "nl.png"),
}

class PowerTradeScene(Scene):
    def construct(self):
        # Chart dimensions
        chart_width = 10
        chart_height = 5
        origin = np.array([-5, -2, 0])

        # Axes scaling
        x_min, x_max = 0, 9  # 10 weeks (0-indexed)
        y_min, y_max = 0, 8000

        def data_to_screen(x_idx, y_val):
            """Convert data coordinates to screen coordinates."""
            x = origin[0] + (x_idx / (x_max - x_min)) * chart_width
            y = origin[1] + ((y_val - y_min) / (y_max - y_min)) * chart_height
            return np.array([x, y, 0])

        # Draw axes
        x_axis = Line(origin, origin + RIGHT * chart_width, color=WHITE, stroke_width=1)
        y_axis = Line(origin, origin + UP * chart_height, color=WHITE, stroke_width=1)

        # X-axis labels (W11 to W20 - 10 weeks matching 10 data points)
        x_labels = VGroup()
        weeks = [f"W{i}" for i in range(11, 21)]  # W11 to W20
        for i, week in enumerate(weeks):
            pos = data_to_screen(i, 0) + DOWN * 0.3
            label = Text(week, font="Calibri", font_size=11, color=GREY_B)
            label.move_to(pos)
            x_labels.add(label)

        # Horizontal grid lines
        grid_lines = VGroup()
        y_ticks = [2000, 4000, 6000, 8000]

        for y_val in y_ticks:
            # Horizontal grid line
            start = data_to_screen(0, y_val)
            end = data_to_screen(9, y_val)
            grid_line = Line(start, end, color=GREY, stroke_width=1, stroke_opacity=0.5)
            grid_lines.add(grid_line)

        # Axis titles
        x_axis_title = Text("Weeks", font="Calibri", font_size=16, color=WHITE)
        x_axis_title.next_to(x_axis, DOWN, buff=0.6)

        y_axis_title = Text("Brand Visibility", font="Calibri", font_size=16, color=WHITE)
        y_axis_title.rotate(90 * DEGREES)
        y_axis_title.next_to(y_axis, LEFT, buff=0.3)

        # Show axes, labels, and grid
        self.play(
            Create(x_axis),
            Create(y_axis),
            run_time=0.625
        )
        self.play(
            FadeIn(x_labels),
            FadeIn(x_axis_title),
            FadeIn(y_axis_title),
            Create(grid_lines),
            run_time=0.625
        )

        # Create series lines and flags
        series_lines = {}
        series_flags = {}
        series_points = {}

        for tag, data in SERIES_DATA.items():
            color = SERIES_COLORS[tag]

            # Create the full path
            points = [data_to_screen(i, val) for i, val in enumerate(data)]
            series_points[tag] = points

            # Create line as a VMobject that we'll animate
            line = VMobject()
            line.set_points_as_corners(points)
            line.set_stroke(color=color, width=4)

            series_lines[tag] = line

            # Create flag image at the final position
            flag = ImageMobject(SERIES_FLAGS[tag])
            flag.set_height(0.28)
            flag.next_to(points[-1], RIGHT, buff=0.15)
            series_flags[tag] = flag

        # Show flags at final positions from the start
        for flag in series_flags.values():
            self.add(flag)

        # Animate all lines "racing" from left to right simultaneously
        line_animations = []
        for tag, line in series_lines.items():
            line_animations.append(Create(line, rate_func=linear))

        self.play(*line_animations, run_time=3.75)

        self.wait(2.5)
