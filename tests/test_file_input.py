from pages.main_comlex_elemnts import MainComplexElemts
import time
def test_upload_file(driver, tmp_path):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    file_to_upload = str(tmp_path / "dummy.txt")
    with open(file_to_upload, "w") as f:
        f.write("test")
    page = MainComplexElemts(driver)
    time.sleep(10)
    assert page.upload_file(file_to_upload)

#     <input type="file" id="myFile" name="filename">
#     The type="file" attribute means you should
#     not attempt to click the "Choose File" button or interact with the operating system's file dialog.
#     You only need to locate this <input> element and use .send_keys(filepath).
