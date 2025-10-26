import pytest

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    page.goto('http://localhost:8000')
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    assert page.inner_text('#result') == 'Calculation Result: 15'

@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '20')
    page.fill('#b', '8')
    page.click('button:text("Subtract")')
    assert page.inner_text('#result') == 'Calculation Result: 12'

@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '6')
    page.fill('#b', '7')
    page.click('button:text("Multiply")')
    assert page.inner_text('#result') == 'Calculation Result: 42'

@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '2')
    page.click('button:text("Divide")')
    # Accept either 5 or 5.0 depending on formatting
    assert page.inner_text('#result') in ['Calculation Result: 5', 'Calculation Result: 5.0']

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'

@pytest.mark.e2e
def test_calculator_invalid_input(page, fastapi_server):
    page.goto('http://localhost:8000')
    # Workaround for input[type=number] — inject invalid value via JavaScript
    page.eval_on_selector('#a', 'el => el.value = "abc"')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    assert "Error" in page.inner_text('#result')
