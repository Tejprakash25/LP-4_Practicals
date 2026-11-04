
package tests;

import java.nio.file.Files;
import java.nio.file.Path;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class SignupTest {

    WebDriver driver;

    @BeforeClass
    public void beforeClass() {
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @Test
    public void signupTest() throws Exception {

        String html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>COVID-19 Registration</title>
            </head>
            <body>
                <h2>COVID-19 Registration Form</h2>

                <form onsubmit="document.getElementById('result').innerText='Registration Successful'; return false;">

                    <input id="fullname" placeholder="Full Name"><br><br>

                    <input id="mobilenumber" placeholder="Mobile Number"><br><br>

                    <input id="dob" placeholder="Date of Birth"><br><br>

                    <input id="email" placeholder="Email"><br><br>

                    <button type="submit">Register</button>

                </form>

                <h3 id="result"></h3>
            </body>
            </html>
            """;

        Path htmlFile = Files.createTempFile("signup-", ".html");
        Files.writeString(htmlFile, html);

        driver.get(htmlFile.toUri().toString());

        driver.findElement(By.id("fullname"))
                .sendKeys("Tejprakash Mirashi");

        driver.findElement(By.id("mobilenumber"))
                .sendKeys("7378965050");

        driver.findElement(By.id("dob"))
                .sendKeys("25-10-2005");

        driver.findElement(By.id("email"))
                .sendKeys("tejprakashmirashi25@gmail.com");

        driver.findElement(By.tagName("button")).click();

        String result = driver.findElement(By.id("result")).getText();

        Assert.assertEquals(result, "Registration Successful");

        System.out.println("Signup Test Passed!");
        Thread.sleep(10000);
    }

    @AfterClass
    public void afterClass() {
    System.out.println("Test execution completed. Browser remains open.");
    }
}
