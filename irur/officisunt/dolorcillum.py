def click_Xpath(driver, num, del_btn):
    """
    Clicks a button identified by its XPath.

    Args:
        driver: The WebDriver instance.
        num: The number of the button to click.
        del_btn: The XPath of the button to click.
    """

    # Find the button by its XPath.
    button = driver.find_elements_by_xpath(del_btn)

    # Click the button.
    button[num].click()
