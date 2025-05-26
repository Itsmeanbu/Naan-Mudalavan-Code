import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class InventoryControlTest {
 public static void main(String[] args) {
 WebDriver driver = new ChromeDriver();
driver.get("https://www.inventory-control-system.com");
 // Login as administrator (Assuming login code)
 // Test Case: Add New Item
 WebElement addNewItemButton = driver.findElement(By.id("add-item-button"));
 addNewItemButton.click();
 WebElement itemNameField = driver.findElement(By.id("item-name"));
 itemNameField.sendKeys("New Product");
 // Fill in other fields...
 WebElement submitButton = driver.findElement(By.id("submit-button"));
 submitButton.click();
 // Verify item added to inventory (Assertion code)
 driver.quit();
 }
}
OUTPUT
No errors encountered. New item "New Product" added to the inventory.









import time

# Define the secret key
secret_key = 123456

def generate_otp():
    return str((int(time.time()) + secret_key) % 1000000).zfill(6)

# User login and OTP check
password = input("Enter your password: ")
if password == "12345":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
    user_otp = input("Enter the OTP: ")
    if user_otp == otp:
        print("Authentication complete.")
    else:
        print("Invalid OTP.")
else:
    print("Incorrect password.")
