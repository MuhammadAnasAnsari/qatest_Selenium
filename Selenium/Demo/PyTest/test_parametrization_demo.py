# To generate the html report: [in which the assets > style.css will generate with report html file]
# 1) instal pytest html   directory>pip install pytest-html
# In terminal / cmd give command 2) directory>pytest --html=report1.html  [name of the report with .html extension]
# =============================================
# To generate / get self contained Html reports:[Use to send the reports with style.css file in it]
# In terminal / cmd give command     dirctory>pytest --html=./reports/report1.html --self-contained-html



import pytest

def sum(a, b):
    return a + b

# Parametrise and take values(inputs and assertion) in the Tuple
@pytest.mark.parametrize("input1, input2, output",
    [
        (3,5,8),
        (5,6,11),
        (9,9,20)
    ]
)
def test_calc_sum_1(input1, input2, output):
    result = sum(input1, input2)
    assert result == output


# def test_calc_sum_2():
#     result = sum(3, 3)
#     assert result == 6
#
#
# def test_calc_sum_3():
#     result = sum(5, 5)
#     assert result == 10
