import smn_caller.charts.pdfs.pdf as pdf
from smn_caller.charts.scale import scale
from smn_caller.charts.colors import colors, color_arr


def get_pdf(sample, x_axis, y_axis, norm_y_axis, cols):
    title = "%s: (SMN1: %s SMN2: %s)" % (sample["sample"], sample["SMN1"], sample["SMN2"])
    pdf_bars = []
    pdf_bars += pdf.x_axis_lines(x_axis, y_axis)
    pdf_bars += pdf.x_axis_tics(x_axis, y_axis)
    pdf_bars += pdf.x_axis_text(x_axis, y_axis)
    pdf_bars += pdf.x_axis_title(x_axis, y_axis)
    pdf_bars += pdf.y_axis_lines(x_axis, norm_y_axis)
    pdf_bars += pdf.y_axis_tics(x_axis, norm_y_axis, "left")
    pdf_bars += pdf.y_axis_text(x_axis, norm_y_axis, "left")
    pdf_bars += pdf.y_axis_title(x_axis, norm_y_axis, "left")
    pdf_bars += pdf.y_axis_tics(x_axis, y_axis, "right")
    pdf_bars += pdf.y_axis_text(x_axis, y_axis, "right")
    pdf_bars += pdf.y_axis_title(x_axis, y_axis, "right")
    pdf_bars += pdf.right_axis_line(x_axis, y_axis)
    pdf_bars += sample_bars(sample, x_axis, norm_y_axis, cols)
    pdf_bars += pdf.title(title, x_axis, y_axis)
    pdf_bars += pdf.get_keys(cols, x_axis, y_axis, element_type="rect")
    pdf_bars += pdf.add_star_to_13(x_axis, y_axis)
    return pdf_bars


def sample_bars(sample_data, x_axis, y_axis, cols):
    hap = sample_data["Median_depth"] / 2
    smn1 = [(x, y / hap) for x, y in sample_data[cols[0]]]
    smn2 = [(x, y / hap) for x, y in sample_data[cols[1]]]

    bars = []
    for x_val, y_val in smn1:
        smn1_bar = get_bar(x_val - 0.4, y_val, x_axis, y_axis, color_arr[0])
        bars += [smn1_bar]

    for x_val, y_val in smn2:
        smn2_bar = get_bar(x_val, y_val, x_axis, y_axis, color_arr[1])
        bars += [smn2_bar]

    return bars


def get_bar(x_val, y_val, x_axis, y_axis, color):
    width = scale(2, x_axis) - scale(1.6, x_axis)
    y = scale(y_val, y_axis)
    height = scale(y_axis["min"], y_axis) - y
    x = scale(x_val, x_axis)
    return pdf.rect(x, y, width, height, border_color=color, fill_color=color, opacity=0.6)
