from pages.main_comlex_elemnts import MainComplexElemts

def test_js_alert_prompt(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    page = MainComplexElemts(driver)
    alert_text = page.trigger_alert()
    assert "Press a button!" in alert_text

    prompt_text = "TestingApp"
    page.trigger_prompt(prompt_text)
    # Optionally assert on prompt handling (behavior depends on JS)

def test_canvas_properties(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    # page map
    page = MainComplexElemts(driver)
    w, h = page.get_canvas_size()
    assert w == "200" and h == "100"
# What is an HTML canvas?
# The HTML <canvas> element provides a drawable region in the page that JavaScript can paint on (pixels, shapes, text, images).
#
# Unlike typical DOM elements (like <div> or <span>), the content you see on a canvas is not made of child elements—it’s just pixels drawn by JS on a 2D (or WebGL) context.
#
# You interact with it using a drawing API via JavaScript, not via DOM children.
#
# What the page is doing
# From the DOM you shared:
#
# There’s a canvas: <canvas id="canpro" style="border:1px solid #d3d3d3;" width="200" height="100"></canvas>
#
# Script draws on it:
#
# var c = document.getElementById("canpro");
#
# var ctx = c.getContext("2d");
#
# ctx.font = "20px Arial";
#
# ctx.fillText("Page Map", 10, 50);