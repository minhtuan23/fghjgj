from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Cấu hình webdriver (dùng Chrome trong ví dụ này)
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Đăng nhập vào Facebook
def login_facebook(email, password):
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)  # Đợi trang load

# Thả Like hoặc Thả Tym
def react_to_post(post_url, reaction="like"):
    # Điều hướng đến bài viết
    driver.get(post_url)
    time.sleep(5)  # Đợi bài viết load

    # Xác định nút Like
    like_button = driver.find_element(By.XPATH, '//div[@aria-label="Like"]')

    # Di chuột để mở menu các reaction (nếu cần thả tym)
    if reaction.lower() != "like":
        actions = ActionChains(driver)
        actions.move_to_element(like_button).perform()
        time.sleep(2)  # Đợi menu hiện

        # Xác định nút reaction (Love - Thả Tym)
        reaction_xpath = {
            "like": '//div[@aria-label="Like"]',
            "love": '//div[@aria-label="Love"]',  # Thả Tym
            # Thêm các reaction khác nếu cần
        }
        reaction_button = driver.find_element(By.XPATH, reaction_xpath.get(reaction.lower(), "like"))
        reaction_button.click()
    else:
        like_button.click()

    time.sleep(2)  # Đợi phản hồi từ Facebook

# Sử dụng
if __name__ == "__main__":
    email = "your_email@example.com"
    password = "your_password"
    post_url = "https://www.facebook.com/example_post"  # URL của bài viết
    reaction_type = "love"  # Có thể chọn: "like", "love", ...

    try:
        login_facebook(email, password)
        react_to_post(post_url, reaction=reaction_type)
    finally:
        driver.quit()  # Đóng trình duyệt sau khi hoàn tất
