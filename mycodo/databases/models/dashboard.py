# coding=utf-8
from mycodo.databases import CRUDMixin
from mycodo.mycodo_flask.extensions import db


class Dashboard(CRUDMixin, db.Model):
    __tablename__ = "graph"  # TODO: rename to 'dashboard'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, unique=True, primary_key=True)
    graph_type = db.Column(db.Text, default=None)
    name = db.Column(db.Text, default='Graph')
    refresh_duration = db.Column(db.Float, default=120)  # How often to add new data and redraw, refresh camera
    width = db.Column(db.Integer, default=12)  # Width of page (1-12, bootstrap col widths)
    height = db.Column(db.Integer, default=400)  # Height (in pixels)

    # Graph options
    pid_ids = db.Column(db.Text, default='')  # store IDs and measurements to display
    relay_ids = db.Column(db.Text, default='')  # store IDs and measurements to display
    math_ids = db.Column(db.Text, default='')  # store Math IDs to display

    sensor_ids_measurements = db.Column(db.Text, default='')  # store IDs and measurements to display
    x_axis_duration = db.Column(db.Float, default=1440)  # X-axis duration (in minutes)
    use_custom_colors = db.Column(db.Boolean, default=False)  # Enable custom colors of graph series
    custom_colors = db.Column(db.Text, default='')  # Custom hex color values (csv)
    enable_navbar = db.Column(db.Boolean, default=False)  # Show navigation bar
    enable_rangeselect = db.Column(db.Boolean, default=False)  # Show range selection buttons
    enable_export = db.Column(db.Boolean, default=False)  # Show export menu
    enable_title = db.Column(db.Boolean, default=False)  # Show title on graph
    enable_auto_refresh = db.Column(db.Boolean, default=True)  # Automatically update graph
    enable_xaxis_reset = db.Column(db.Boolean, default=True)  # Reset the graph x-axis min/max on update
    enable_graph_shift = db.Column(db.Boolean, default=False)  # Set HighStock addPoint() shift=true/false
    enable_manual_y_axis = db.Column(db.Boolean, default=False)  # Manual selection of y-axis min/max
    enable_start_on_tick = db.Column(db.Boolean, default=True)  # Enable HighCharts startOnTick
    enable_end_on_tick = db.Column(db.Boolean, default=True)  # Enable HighCharts endOnTick
    enable_align_ticks = db.Column(db.Boolean, default=True)  # Enable HighCharts alignTicks
    custom_yaxes = db.Column(db.Text, default='')  # Custom minimum and maximum y-axes
    decimal_places = db.Column(db.Integer, default=1)  # Number of decimal places for displayed value

    # Gauge options
    max_measure_age = db.Column(db.Float, default=120.0)  # Only show measurements if they are younger than this age
    range_colors = db.Column(db.Text, default='')  # Custom hex color values and gauge range
    enable_timestamp = db.Column(db.Boolean, default=True)  # Show timestamp for displayed gauge value

    # Graph and Gauge options
    y_axis_min = db.Column(db.Float, default=None)  # x-axis minimum
    y_axis_max = db.Column(db.Float, default=None)  # x-axis maximum

    # Output options
    output_ids = db.Column(db.Text, default='')  # store Output IDs to display
    font_em_value = db.Column(db.Float, default=1.0)  # Font size of value
    font_em_timestamp = db.Column(db.Float, default=1.0)  # Font size of timestamp
    enable_output_controls = db.Column(db.Boolean, default=True)  # Show output controls on dashboard element

    # PID options
    enable_pid_info = db.Column(db.Boolean, default=True)  # Display detailed information about the PID

    # Camera options
    camera_id = db.Column(db.Text, default='')  # store camera ID to display
    camera_image_type = db.Column(db.Text, default='')  # save new image, overwrite old, display last timelapse
    camera_max_age = db.Column(db.Integer, default=360)  # max camera image age before "No new image" shown

    def __repr__(self):
        return "<{cls}(id={s.id})>".format(s=self, cls=self.__class__.__name__)
