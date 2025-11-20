from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_dominos_audit_form(driver, wait):
    """
    Automated form filling for Domino's Store Audit Form
    """
    
    # Switch to iframe if form is inside iframe
    try:
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)
        print("Switched to iframe")
    except:
        print("No iframe found, continuing with main page")
    
    # Wait for form to load
    time.sleep(3)
    
    # Store Information (pre-filled, disabled fields - skip)
    
    # Audit Date
    audit_date = wait.until(EC.element_to_be_clickable((By.NAME, "auditDate")))
    driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -100);", audit_date)
    time.sleep(1)
    audit_date.clear()
    audit_date.send_keys("2024-01-15")
    
    # Time Slot
    time_slot = Select(wait.until(EC.element_to_be_clickable((By.NAME, "TimeSlot"))))
    time_slot.select_by_value("7 PM – 11 PM → Dinner")
    
    # Exterior Infra - Signage
    signage_element = wait.until(EC.element_to_be_clickable((By.NAME, "wasTheSignageOutsideTheStoreCleanAndWellLitInTheEvening")))
    driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -100);", signage_element)
    time.sleep(1)
    signage_select = Select(signage_element)
    signage_select.select_by_value("yes")
    
    # Upload signage image (if required)
    signage_image = driver.find_element(By.NAME, "imageOfSignage")
    driver.execute_script("window.scrollTo(0, arguments[0].offsetTop - 200);", signage_image)
    time.sleep(2)
    signage_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    # Signage remarks
    signage_remarks = driver.find_element(By.NAME, "signageRemarks")
    driver.execute_script("window.scrollTo(0, arguments[0].offsetTop - 200);", signage_remarks)
    time.sleep(2)
    signage_remarks.send_keys("Signage is clean and well-lit")
    
    # Delivery Vehicles
    vehicles_element = driver.find_element(By.NAME, "wereTheDominosDeliveryVehiclesParkedCorrectlyWereTheyCleanAndWellMaintained")
    driver.execute_script("window.scrollTo(0, arguments[0].offsetTop - 200);", vehicles_element)
    time.sleep(2)
    vehicles_select = Select(vehicles_element)
    vehicles_select.select_by_value("yes")
    
    # Upload vehicle image
    vehicle_image = driver.find_element(By.NAME, "imageOfVehicles")
    vehicle_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    # Vehicle remarks
    vehicle_remarks = driver.find_element(By.NAME, "vehiclesRemarks")
    vehicle_remarks.send_keys("Vehicles are properly parked and maintained")
    
    # Marketing Collateral - Inside Banner
    inside_banner_element = driver.find_element(By.NAME, "wasStandyBannerPlacedAndVisibleInsideTheStoreAsPerVos")
    driver.execute_script("arguments[0].scrollIntoView(true);", inside_banner_element)
    inside_banner_select = Select(inside_banner_element)
    inside_banner_select.select_by_value("yes")
    
    inside_banner_image = driver.find_element(By.NAME, "imageOfInsideBanner")
    inside_banner_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    inside_banner_remarks = driver.find_element(By.NAME, "insideBannerRemarks")
    inside_banner_remarks.send_keys("Banner is properly placed and visible")
    
    # Outside Banner
    outside_banner_element = driver.find_element(By.NAME, "wasPosterStandyBannerVisibleOutsideTheStoreAsPerVos")
    driver.execute_script("arguments[0].scrollIntoView(true);", outside_banner_element)
    outside_banner_select = Select(outside_banner_element)
    outside_banner_select.select_by_value("yes")
    
    outside_banner_image = driver.find_element(By.NAME, "imageOfOutsideBanner")
    outside_banner_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    outside_banner_remarks = driver.find_element(By.NAME, "outsideBannerRemarks")
    outside_banner_remarks.send_keys("Outside banner is visible and well-positioned")
    
    # Ambience - Store Infra
    temperature_element = driver.find_element(By.NAME, "wasTheTemperatureInsideTheRestaurantsDiningAreaAdequatelyMaintainedComfortableAsPerTheWeather")
    driver.execute_script("arguments[0].scrollIntoView(true);", temperature_element)
    temperature_select = Select(temperature_element)
    temperature_select.select_by_value("yes")
    
    dining_area_remarks = driver.find_element(By.NAME, "diningAreaRemarks")
    dining_area_remarks.send_keys("Temperature is comfortable and well-maintained")
    
    # Customer Area Furniture
    furniture_element = driver.find_element(By.NAME, "customerAreaFurnitureWereTablesChairsSofaTilesWallSealingWellMaintainedNoDamageWearTear")
    driver.execute_script("arguments[0].scrollIntoView(true);", furniture_element)
    furniture_select = Select(furniture_element)
    furniture_select.select_by_value("yes")
    
    furniture_image = driver.find_element(By.NAME, "imageOfCustomerAreaFurniture")
    furniture_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    furniture_remarks = driver.find_element(By.NAME, "customerAreaFurnitureRemarks")
    furniture_remarks.send_keys("All furniture is well-maintained with no damage")
    
    # Digital Menu Board
    dmb_element = driver.find_element(By.NAME, "wasTheDigitalMenuBoardDmbWorkingProperly")
    driver.execute_script("arguments[0].scrollIntoView(true);", dmb_element)
    dmb_select = Select(dmb_element)
    dmb_select.select_by_value("yes")
    
    dmb_image = driver.find_element(By.NAME, "imageOfDmb")
    dmb_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    dmb_remarks = driver.find_element(By.NAME, "dmbRemarks")
    dmb_remarks.send_keys("Digital menu board is working properly")
    
    # No Bill Board
    no_bill_element = driver.find_element(By.NAME, "wasTheNoBillItsOurTreatBoardAvailableVisibleAtNearOrderingCounterOrNot")
    driver.execute_script("arguments[0].scrollIntoView(true);", no_bill_element)
    no_bill_select = Select(no_bill_element)
    no_bill_select.select_by_value("yes")
    
    board_image = driver.find_element(By.NAME, "imageOfBoard")
    board_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    board_remarks = driver.find_element(By.NAME, "boardRemarks")
    board_remarks.send_keys("No bill board is visible at ordering counter")
    
    # Order Display Screen
    order_display_element = driver.find_element(By.NAME, "wasTheOrderDisplayScreenAvailableAndWasItDisplayingOrdersReadyToEat")
    driver.execute_script("arguments[0].scrollIntoView(true);", order_display_element)
    order_display_select = Select(order_display_element)
    order_display_select.select_by_value("yes")
    
    order_display_image = driver.find_element(By.NAME, "imageOfOrderDisplayScreen")
    order_display_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    order_display_remarks = driver.find_element(By.NAME, "orderDisplayScreenRemarks")
    order_display_remarks.send_keys("Order display screen is working and showing orders")
    
    # Cleanliness - Floor
    floor_element = driver.find_element(By.NAME, "wasTheFloorNeatAndClean")
    driver.execute_script("arguments[0].scrollIntoView(true);", floor_element)
    floor_select = Select(floor_element)
    floor_select.select_by_value("yes")
    
    floor_image = driver.find_element(By.NAME, "imageOfFloorNeatAndClean")
    floor_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    floor_remarks = driver.find_element(By.NAME, "floorNeatAndCleanRemarks")
    floor_remarks.send_keys("Floor is neat and clean")
    
    # Washroom
    washroom_element = driver.find_element(By.NAME, "wasTheWashroomNeatAndClean")
    driver.execute_script("arguments[0].scrollIntoView(true);", washroom_element)
    washroom_select = Select(washroom_element)
    washroom_select.select_by_value("yes")
    
    washroom_image = driver.find_element(By.NAME, "imageOfWashroomNeatAndClean")
    washroom_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    washroom_remarks = driver.find_element(By.NAME, "washroomNeatAndCleanRemarks")
    washroom_remarks.send_keys("Washroom is neat and clean")
    
    # Staff Behavior - Dress Code
    dress_code_element = driver.find_element(By.NAME, "wasStaffFollowingTheDressCode")
    driver.execute_script("arguments[0].scrollIntoView(true);", dress_code_element)
    dress_code_select = Select(dress_code_element)
    dress_code_select.select_by_value("yes")
    
    staff_dress_image = driver.find_element(By.NAME, "imageOfStaffDressCode")
    staff_dress_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    staff_dress_remarks = driver.find_element(By.NAME, "staffDressCodeRemarks")
    staff_dress_remarks.send_keys("Staff is following proper dress code")
    
    # Staff Gear
    staff_gear_element = driver.find_element(By.NAME, "wasStaffWearingAdequateGearHairNetCaps")
    driver.execute_script("arguments[0].scrollIntoView(true);", staff_gear_element)
    staff_gear_select = Select(staff_gear_element)
    staff_gear_select.select_by_value("yes")
    
    staff_image = driver.find_element(By.NAME, "imageOfStaff")
    staff_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    staff_remarks = driver.find_element(By.NAME, "staffRemarks")
    staff_remarks.send_keys("Staff is wearing adequate gear including hair nets and caps")
    
    # Greetings
    greeting_element = driver.find_element(By.NAME, "didTheStaffAcknowledgeOrGreetTheCustomer")
    driver.execute_script("arguments[0].scrollIntoView(true);", greeting_element)
    greeting_select = Select(greeting_element)
    greeting_select.select_by_value("yes")
    
    greeting_remarks = driver.find_element(By.NAME, "greetTheCustomerRemarks")
    greeting_remarks.send_keys("Staff properly acknowledged and greeted customers")
    
    # Drinking Water
    water_element = driver.find_element(By.NAME, "wasTheDrinkingWaterAvailableInsideTheStoreIfNotDidStaffProvideWaterUponAsking")
    driver.execute_script("arguments[0].scrollIntoView(true);", water_element)
    water_select = Select(water_element)
    water_select.select_by_value("yes")
    
    water_image = driver.find_element(By.NAME, "imageOfDrinkingWater")
    water_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    water_remarks = driver.find_element(By.NAME, "drinkingWaterRemarks")
    water_remarks.send_keys("Drinking water is available in the store")
    
    # Staff Courtesy
    courtesy_element = driver.find_element(By.NAME, "wasTheStaffCourteousAndPoliteWithTheCustomer")
    driver.execute_script("arguments[0].scrollIntoView(true);", courtesy_element)
    courtesy_select = Select(courtesy_element)
    courtesy_select.select_by_value("yes")
    
    courtesy_remarks = driver.find_element(By.NAME, "staffCourteousAndPoliteRemarks")
    courtesy_remarks.send_keys("Staff was courteous and polite with customers")
    
    # Cross-talking
    cross_talk_element = driver.find_element(By.NAME, "wasStaffObservedCrossTalkingOrSpeakingOnThePhoneWhileTakingOrders")
    driver.execute_script("arguments[0].scrollIntoView(true);", cross_talk_element)
    cross_talk_select = Select(cross_talk_element)
    cross_talk_select.select_by_value("no")
    
    cross_talk_remarks = driver.find_element(By.NAME, "crossTalkingRemarks")
    cross_talk_remarks.send_keys("No cross-talking or phone usage observed during order taking")
    
    # Ordering & Service - Staff Availability
    staff_availability_element = driver.find_element(By.NAME, "wasStaffAvailableAtAllOrderCountersInCaseOfHighQueueAtTheStore")
    driver.execute_script("arguments[0].scrollIntoView(true);", staff_availability_element)
    staff_availability_select = Select(staff_availability_element)
    staff_availability_select.select_by_value("yes")
    
    staff_counter_image = driver.find_element(By.NAME, "imageOfStaffAtOrderCounter")
    staff_counter_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    staff_counter_remarks = driver.find_element(By.NAME, "staffAtOrderCounterRemarks")
    staff_counter_remarks.send_keys("Staff was available at all order counters")
    
    # Upselling
    upsell_element = driver.find_element(By.NAME, "didStaffShareTheOngoingOffersNewLaunchesEtcAndTryToUpsellCrossSell")
    driver.execute_script("arguments[0].scrollIntoView(true);", upsell_element)
    upsell_select = Select(upsell_element)
    upsell_select.select_by_value("yes")
    
    upsell_remarks = driver.find_element(By.NAME, "ongoingOffersRemarks")
    upsell_remarks.send_keys("Staff shared ongoing offers and attempted upselling")
    
    # Invoice
    invoice_element = driver.find_element(By.NAME, "didYouReceiveAnInvoiceOnSms")
    driver.execute_script("arguments[0].scrollIntoView(true);", invoice_element)
    invoice_select = Select(invoice_element)
    invoice_select.select_by_value("yes")
    
    invoice_image = driver.find_element(By.NAME, "imageOfInvoice")
    invoice_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    invoice_remarks = driver.find_element(By.NAME, "invoiceRemarks")
    invoice_remarks.send_keys("Invoice received via SMS")
    
    # Food Serving Time
    serving_time_element = driver.find_element(By.NAME, "didStaffCommunicateTheFoodServingTime")
    driver.execute_script("arguments[0].scrollIntoView(true);", serving_time_element)
    serving_time_select = Select(serving_time_element)
    serving_time_select.select_by_value("yes")
    
    serving_time_remarks = driver.find_element(By.NAME, "foodServingTimeRemarks")
    serving_time_remarks.send_keys("Staff communicated the food serving time")
    
    # Pizza Box with Slip
    pizza_slip_element = driver.find_element(By.NAME, "didYouReceiveYourPizzaBoxWithSlipAttachedToIt")
    driver.execute_script("arguments[0].scrollIntoView(true);", pizza_slip_element)
    pizza_slip_select = Select(pizza_slip_element)
    pizza_slip_select.select_by_value("yes")
    
    order_image = driver.find_element(By.NAME, "imageOfOrder")
    order_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    order_slip_remarks = driver.find_element(By.NAME, "orderWithSlipRemarks")
    order_slip_remarks.send_keys("Pizza box received with slip attached")
    
    # Food Quality - Hot Food
    hot_food_element = driver.find_element(By.NAME, "wasTheFoodServedHotCaptureTheProductName")
    driver.execute_script("arguments[0].scrollIntoView(true);", hot_food_element)
    hot_food_select = Select(hot_food_element)
    hot_food_select.select_by_value("yes")
    
    product_image = driver.find_element(By.NAME, "imageOfOrderWithProductName")
    product_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    product_remarks = driver.find_element(By.NAME, "orderWithProductNameRemarks")
    product_remarks.send_keys("Margherita Pizza - served hot")
    
    # Toppings
    toppings_element = driver.find_element(By.NAME, "didYouFindAdequateToppingsCheeseEtcOnYourPizza")
    driver.execute_script("arguments[0].scrollIntoView(true);", toppings_element)
    toppings_select = Select(toppings_element)
    toppings_select.select_by_value("yes")
    
    inside_image = driver.find_element(By.NAME, "imageOfOrderInside")
    inside_image.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")
    
    inside_remarks = driver.find_element(By.NAME, "orderInsideRemarks")
    inside_remarks.send_keys("Adequate toppings and cheese found on pizza")
    
    # Appearance
    appearance_element = driver.find_element(By.NAME, "didYouLikeTheAppearanceOfTheProduct")
    driver.execute_script("arguments[0].scrollIntoView(true);", appearance_element)
    appearance_select = Select(appearance_element)
    appearance_select.select_by_value("yes")
    
    appearance_remarks = driver.find_element(By.NAME, "appearanceOfTheProductRemarks")
    appearance_remarks.send_keys("Product appearance was appealing and well-presented")
    
    # Baking Quality
    baking_element = driver.find_element(By.NAME, "wasTheProductBakedOrCookedProperly")
    driver.execute_script("arguments[0].scrollIntoView(true);", baking_element)
    baking_select = Select(baking_element)
    baking_select.select_by_value("yes")
    
    baking_remarks = driver.find_element(By.NAME, "productBakedRemarks")
    baking_remarks.send_keys("Product was properly baked and cooked")
    
    # Taste
    taste_element = driver.find_element(By.NAME, "didYouLikeTheTasteOfTheFoodIfNotWhatWasTheProblem")
    driver.execute_script("arguments[0].scrollIntoView(true);", taste_element)
    taste_select = Select(taste_element)
    taste_select.select_by_value("yes")
    
    taste_remarks = driver.find_element(By.NAME, "tasteOfTheFoodRemarks")
    taste_remarks.send_keys("Food taste was excellent, no issues found")
    
    # Red Alert
    red_alert = driver.find_element(By.NAME, "redAlert")
    driver.execute_script("arguments[0].scrollIntoView(true);", red_alert)
    red_alert.send_keys("No red alerts or critical issues observed during the audit")
    
    # Upload audit video
    video_upload = driver.find_element(By.NAME, "uploadAuditVideoFile")
    driver.execute_script("arguments[0].scrollIntoView(true);", video_upload)
    video_upload.send_keys("/Users/himanshu.tiwari/Okaygo/screenshot.png")  # Using image as placeholder
    
    # Submit form
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' or contains(text(), 'Submit')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()
    
    print("Form filled and submitted successfully!")
    
    # Switch back to main content
    driver.switch_to.default_content()

if __name__ == "__main__":
    # Test the form filling function
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    
    # Navigate to form URL (replace with actual form URL)
    # driver.get("FORM_URL_HERE")
    
    # fill_dominos_audit_form(driver, wait)
    
    driver.quit()