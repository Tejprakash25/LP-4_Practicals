package tests;

import org.testng.Assert;
import org.testng.annotations.Test;

public class RegexTest {

    @Test
    public void testEmail() {
        String email = "test@gmail.com";
        Assert.assertTrue(email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"));
    }

    @Test
    public void testMobile() {
        String mobile = "9876543210";
        Assert.assertTrue(mobile.matches("^[0-9]{10}$"));
    }

    @Test
    public void testName() {
        String name = "Atharva Jagtap";
        Assert.assertTrue(name.matches("^[A-Za-z ]+$"));
    }

    @Test
    public void testPassword() {
        String password = "Test@123";
        Assert.assertTrue(password.matches("^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=!]).{8,}$"));
    }

    @Test
    public void testDate() {
        String date = "09-04-2000";
        Assert.assertTrue(date.matches("^\\d{2}-\\d{2}-\\d{4}$"));
    }
}
