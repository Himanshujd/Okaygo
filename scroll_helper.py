def scroll_and_interact(driver, element):
    """Scroll to element and ensure it's visible before interaction"""
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    driver.implicitly_wait(2)
    return element