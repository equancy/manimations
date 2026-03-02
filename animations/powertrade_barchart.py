from manim import *
import numpy as np


# Original Prompt:
# write a script powertrade_radar.py to generate a radar graph with the following axis:
# - Fragance
# - Women Fragance
# - Men Fragance
# - Skincare
# - Make-up
# - Homepage
# 
# Make two profiles lines on the radar, one called "My Brand", the other "Competitor".
# Use vivid colors for the two profiles lines.
# Generate fake data for each profile, each dimension ranging from 0 to 100.
# 
# Make an animation when first drawing the radar, revealing it in a clockwise sweep.
# Use three intermediate thin lines to tick the level on each axis.


# Dataset
DATA = {
    "Pinalli IT": {"My Brand": 41000, "Competitor": 10000},
    "Douglas IT": {"My Brand": 37000, "Competitor": 8000},
    "Douglas DE": {"My Brand": 37000, "Competitor": 24000},
    "Douglas ES": {"My Brand": 27000, "Competitor": 11000},
    "Nocibe FR": {"My Brand": 23000, "Competitor": 39000},
    "Flaconi DE": {"My Brand": 14000, "Competitor": 14000},
    "Marionnaud FR": {"My Brand": 11000, "Competitor": 20000},
    "Sephora IT": {"My Brand": 9000, "Competitor": 10000},
    "Perfumeria Julia ES": {"My Brand": 7000, "Competitor": 17000},
    "Douglas NL": {"My Brand": 3000, "Competitor": 11000},
    "Druni ES": {"My Brand": 3000, "Competitor": 9000},
    "Arenal ES": {"My Brand": 2000, "Competitor": 14000},
    "Ici Paris XL NL": {"My Brand": 2000, "Competitor": 4000},
    "Sephora FR": {"My Brand": 1000, "Competitor": 10000},
    "Sephora DE": {"My Brand": 1000, "Competitor": 11000},
    "Marionnaud IT": {"My Brand": 1000, "Competitor": 12000},
}

# Colors matching powertrade_radar.py
PROFILE_COLORS = {
    "My Brand": "#00AAFF",      # Vivid blue
    "Competitor": "#FF3366",    # Vivid pink-red
}


class BarChartScene(Scene):
    def construct(self):
        # Chart configuration
        chart_width = 12
        chart_height = 5
        origin = np.array([-6, -2.5, 0])

        sites = list(DATA.keys())
        num_sites = len(sites)

        # Find max value for scaling
        max_value = max(
            max(values["My Brand"], values["Competitor"])
            for values in DATA.values()
        )
        # Round up to nice number
        max_value = 45000

        # Bar dimensions
        group_width = chart_width / num_sites
        bar_width = group_width * 0.35
        bar_gap = group_width * 0.05

        def value_to_height(value):
            return (value / max_value) * chart_height

        def get_bar_x(site_index, is_competitor=False):
            group_center = origin[0] + (site_index + 0.5) * group_width
            if is_competitor:
                return group_center + bar_gap / 2
            else:
                return group_center - bar_width - bar_gap / 2

        # Create axes
        x_axis = Line(origin, origin + RIGHT * chart_width, color=WHITE, stroke_width=1)
        y_axis = Line(origin, origin + UP * chart_height, color=WHITE, stroke_width=1)

        # Grid lines (no y-axis tick labels)
        grid_lines = VGroup()
        y_ticks = [10000, 20000, 30000, 40000]

        for y_val in y_ticks:
            height = value_to_height(y_val)
            # Horizontal grid line
            start = origin + UP * height
            end = origin + UP * height + RIGHT * chart_width
            grid_line = Line(start, end, color=GREY, stroke_width=0.5, stroke_opacity=0.3)
            grid_lines.add(grid_line)

        # Axis titles
        x_axis_title = Text("Websites", font="Calibri", font_size=16, color=WHITE)
        x_axis_title.next_to(x_axis, DOWN, buff=1.2)

        y_axis_title = Text("Visibility", font="Calibri", font_size=16, color=WHITE)
        y_axis_title.rotate(90 * DEGREES)
        y_axis_title.next_to(y_axis, LEFT, buff=0.3)

        # X-axis labels (site names)
        x_labels = VGroup()
        for i, site in enumerate(sites):
            group_center_x = origin[0] + (i + 0.5) * group_width
            label = Text(site, font="Calibri", font_size=8, color=GREY_B)
            label.rotate(-30 * DEGREES)
            label.move_to([group_center_x, origin[1] - 0.4, 0])
            x_labels.add(label)

        # Create bar outlines and fills
        my_brand_outlines = VGroup()
        my_brand_fills = VGroup()
        competitor_outlines = VGroup()
        competitor_fills = VGroup()

        for i, site in enumerate(sites):
            my_brand_value = DATA[site]["My Brand"]
            competitor_value = DATA[site]["Competitor"]

            my_brand_height = value_to_height(my_brand_value)
            competitor_height = value_to_height(competitor_value)

            my_brand_x = get_bar_x(i, is_competitor=False)
            competitor_x = get_bar_x(i, is_competitor=True)

            # My Brand bar
            my_brand_rect = Rectangle(
                width=bar_width,
                height=my_brand_height,
                stroke_color=PROFILE_COLORS["My Brand"],
                stroke_width=2,
                fill_opacity=0
            )
            my_brand_rect.move_to([
                my_brand_x + bar_width / 2,
                origin[1] + my_brand_height / 2,
                0
            ])
            my_brand_outlines.add(my_brand_rect)

            my_brand_fill = Rectangle(
                width=bar_width,
                height=my_brand_height,
                stroke_width=0,
                fill_color=PROFILE_COLORS["My Brand"],
                fill_opacity=0.7
            )
            my_brand_fill.move_to([
                my_brand_x + bar_width / 2,
                origin[1] + my_brand_height / 2,
                0
            ])
            my_brand_fills.add(my_brand_fill)

            # Competitor bar
            competitor_rect = Rectangle(
                width=bar_width,
                height=competitor_height,
                stroke_color=PROFILE_COLORS["Competitor"],
                stroke_width=2,
                fill_opacity=0
            )
            competitor_rect.move_to([
                competitor_x + bar_width / 2,
                origin[1] + competitor_height / 2,
                0
            ])
            competitor_outlines.add(competitor_rect)

            competitor_fill = Rectangle(
                width=bar_width,
                height=competitor_height,
                stroke_width=0,
                fill_color=PROFILE_COLORS["Competitor"],
                fill_opacity=0.7
            )
            competitor_fill.move_to([
                competitor_x + bar_width / 2,
                origin[1] + competitor_height / 2,
                0
            ])
            competitor_fills.add(competitor_fill)

        # Legend
        legend = VGroup()
        for profile_name in ["My Brand", "Competitor"]:
            color = PROFILE_COLORS[profile_name]
            square = Square(side_length=0.2, color=color, fill_opacity=0.7, stroke_width=2)
            square.set_fill(color=color, opacity=0.7)
            square.set_stroke(color=color, width=2)
            label = Text(profile_name, font="Calibri", font_size=14, color=color)
            label.next_to(square, RIGHT, buff=0.15)
            legend_item = VGroup(square, label)
            legend.add(legend_item)

        legend.arrange(RIGHT, buff=0.5)
        legend.move_to([0, origin[1] + chart_height + 0.5, 0])

        # Animation sequence
        # 1. Show axes and grid
        self.play(
            Create(x_axis),
            Create(y_axis),
            run_time=0.9375
        )

        self.play(
            Create(grid_lines),
            FadeIn(x_axis_title),
            FadeIn(y_axis_title),
            run_time=0.9375
        )

        self.play(
            FadeIn(x_labels, lag_ratio=0.05),
            run_time=1.25
        )

        # 2. Draw bar outlines (left to right)
        self.play(
            *[Create(outline) for outline in my_brand_outlines],
            *[Create(outline) for outline in competitor_outlines],
            lag_ratio=0.02,
            run_time=2.5
        )

        # 3. Fill bars (animate fill growing from bottom)
        fill_animations = []
        for fill in my_brand_fills:
            fill_animations.append(FadeIn(fill, shift=UP * 0.1))
        for fill in competitor_fills:
            fill_animations.append(FadeIn(fill, shift=UP * 0.1))

        self.play(
            *fill_animations,
            lag_ratio=0.02,
            run_time=1.875
        )

        # 4. Show legend
        self.play(
            FadeIn(legend),
            run_time=0.625
        )

        self.wait(2.5)
