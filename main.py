import math
from typing import List

import matplotlib.pyplot as plt

_OUTPUT_PATH = "derivatives.pdf"
_FUNCTIONS = [
    "C",
    "x^n",
    "x",
    "\\frac{1}{x}",
    "\\sqrt{x}",
    "a^x",
    "e^x",
    "\\log_a{x}",
    "\\ln{x}",
    "\\sin{x}",
    "\\cos{x}",
    "\\tan{x}",
    "\\cot{x}",
    "\\arcsin{x}",
    "\\arccos{x}",
    "\\arctan{x}",
]

_D_OVER_DX = "\\frac{d}{dx}"


def _generate_derivatives_to_pdf(
    latex_functions: List[str],
    output_path: str,
    use_dx: bool = False,
) -> None:
    fig = plt.figure(figsize=(6, 6), linewidth=1, edgecolor="black")

    x_start_position = 0.1
    y_start_position = 0.95
    x_position = x_start_position
    y_position = y_start_position
    x_change = 0.2
    y_change = -0.1

    columns_amount = 4
    functions_size = len(latex_functions)
    functions_per_column = math.ceil(functions_size / columns_amount)
    function_counter = 0

    for function in latex_functions:
        if not use_dx:
            text = f"$({function})' =$"
        else:
            text = f"${_D_OVER_DX}({function}) =$"
        fig.text(x_position, y_position, text)

        function_counter += 1
        if function_counter >= functions_per_column:
            function_counter = 0
            y_position = y_start_position
            x_position += x_change
        else:
            y_position += y_change

    plt.savefig(output_path, format="pdf")
    plt.close(fig)


def main() -> None:
    _generate_derivatives_to_pdf(_FUNCTIONS, _OUTPUT_PATH, use_dx=True)


if __name__ == "__main__":
    main()
