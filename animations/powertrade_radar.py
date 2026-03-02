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


# Radar chart configuration
AXES = ["Fragrance", "Women Fragrance", "Men Fragrance", "Skincare", "Make-up", "Homepage"]
TEXTS_CORRECTIONS = [(0, -0.2), (0.2, 0), (0.2, 0), (0, 0.2), (0, 0), (0, 0)]
NUM_AXES = len(AXES)

# Fake data for each profile (0-100 scale)
PROFILES = {
    "My Brand": [85, 72, 45, 60, 78, 92],
    "Competitor": [55, 88, 70, 82, 45, 65],
}

# Vivid colors for profiles
PROFILE_COLORS = {
    "My Brand": "#00AAFF",      # Vivid blue
    "Competitor": "#FF3366",    # Vivid pink-red
}


class RadarChartScene(Scene):
    def construct(self):
        # Chart configuration
        center = ORIGIN
        max_radius = 2.5
        num_levels = 3  # Three intermediate tick lines

        # Calculate angles for each axis (starting from top, going clockwise)
        angles = [PI / 2 - (2 * PI * i / NUM_AXES) for i in range(NUM_AXES)]

        def polar_to_cartesian(angle, radius):
            """Convert polar coordinates to cartesian."""
            return center + radius * np.array([np.cos(angle), np.sin(angle), 0])

        # Create axis lines
        axis_lines = VGroup()
        for angle in angles:
            line = Line(center, polar_to_cartesian(angle, max_radius), color=GREY, stroke_width=1)
            axis_lines.add(line)

        # Create axis labels
        axis_labels = VGroup()
        for i, (angle, label_text) in enumerate(zip(angles, AXES)):
            label = Text(label_text, font="Calibri", font_size=14, color=WHITE)
            # Position labels slightly outside the chart, with corrections
            correction = TEXTS_CORRECTIONS[i]
            label_pos = polar_to_cartesian(angle, max_radius + 0.4) + np.array([correction[0], correction[1], 0])
            label.move_to(label_pos)
            axis_labels.add(label)

        # Create intermediate level lines (thin grey polygons at 25%, 50%, 75%)
        level_lines = VGroup()
        level_percentages = [0.25, 0.5, 0.75]
        for pct in level_percentages:
            radius = max_radius * pct
            points = [polar_to_cartesian(angle, radius) for angle in angles]
            points.append(points[0])  # Close the polygon
            level_polygon = VMobject()
            level_polygon.set_points_as_corners(points)
            level_polygon.set_stroke(color=GREY, width=1, opacity=0.5)
            level_lines.add(level_polygon)

        # Create outer boundary
        outer_points = [polar_to_cartesian(angle, max_radius) for angle in angles]
        outer_points.append(outer_points[0])
        outer_boundary = VMobject()
        outer_boundary.set_points_as_corners(outer_points)
        outer_boundary.set_stroke(color=WHITE, width=2)

        # Create profile polygons
        profile_shapes = {}
        profile_labels = {}

        for profile_name, data in PROFILES.items():
            color = PROFILE_COLORS[profile_name]
            # Convert data to radius values
            radii = [val / 100 * max_radius for val in data]
            points = [polar_to_cartesian(angles[i], radii[i]) for i in range(NUM_AXES)]
            points.append(points[0])  # Close the polygon

            # Create polygon
            polygon = VMobject()
            polygon.set_points_as_corners(points)
            polygon.set_stroke(color=color, width=3)
            polygon.set_fill(color=color, opacity=0.2)

            profile_shapes[profile_name] = polygon

            # Create label
            label = Text(profile_name, font="Calibri", font_size=16, color=color)
            profile_labels[profile_name] = label

        # Position legend in bottom left quadrant
        legend = VGroup()
        for i, (profile_name, label) in enumerate(profile_labels.items()):
            color = PROFILE_COLORS[profile_name]
            # Use small square instead of line
            square_indicator = Square(side_length=0.2, color=color, fill_opacity=1, stroke_width=0)
            square_indicator.set_fill(color=color, opacity=1)
            label.next_to(square_indicator, RIGHT, buff=0.15)
            legend_item = VGroup(square_indicator, label)
            legend.add(legend_item)

        # Arrange legend items vertically and position in bottom left
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        legend.move_to([-5, -2.5, 0], aligned_edge=LEFT)

        # Animation: Clockwise sweep reveal
        # Create a sweeping sector that reveals the chart

        # First, create all elements but make them invisible
        all_radar_elements = VGroup(axis_lines, level_lines, outer_boundary)

        # Animate the radar structure appearing with a clockwise sweep
        self.play(
            Create(axis_lines, lag_ratio=0.1),
            run_time=1.25
        )

        self.play(
            Create(level_lines, lag_ratio=0.2),
            Create(outer_boundary),
            run_time=1.25
        )

        self.play(
            FadeIn(axis_labels, lag_ratio=0.1),
            run_time=0.9375
        )

        # Animate profile polygons
        profile_list = list(profile_shapes.values())
        self.play(
            *[Create(polygon, rate_func=linear) for polygon in profile_list],
            run_time=1.875
        )

        # Show legend
        self.play(
            FadeIn(legend),
            run_time=0.625
        )

        self.wait(2.5)
