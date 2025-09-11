import cv2

original_image = None
scaled_image_1_5 = None
scaled_image_1_25_0_75 = None

while True:
    print("\nMenu:")
    print("a) Read an image")
    print("b) Scale image by 1.5")
    print("c) Save above scaled image")
    print("d) Scale original image - fx: 1.25, fy: 0.75")
    print("e) Save above scaled image")
    print("f) Change original image size to (300,300)")
    print("x) Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        file_path = input("Enter the path of the image: ")
        original_image = cv2.imread(file_path)
        if original_image is None:
            print("Error: Unable to read the image. Please check the file path.")
        else:
            cv2.imshow("Original Image", original_image)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
    elif choice == 'b':
        if original_image is not None:
            scaled_image_1_5 = cv2.resize(original_image, None, fx=1.5, fy=1.5)
            print("Image scaled by 1.5x")
            cv2.imshow("Scaled Image (1.5x)", scaled_image_1_5)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
        else:
            print("Please read an image first.")
    elif choice == 'c':
        if scaled_image_1_5 is not None:
            cv2.imwrite("scaled_image_1.5.jpg", scaled_image_1_5)
            print("Image saved successfully.")
        else:
            print("Please scale the image first.")
    elif choice == 'd':
        if original_image is not None:
            scaled_image_1_25_0_75 = cv2.resize(original_image, None, fx=1.25, fy=0.75)
            print("Image scaled by fx: 1.25, fy: 0.75")
            cv2.imshow("Scaled Image (1.25x, 0.75y)", scaled_image_1_25_0_75)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
        else:
            print("Please read an image first.")
    elif choice == 'e':
        if scaled_image_1_25_0_75 is not None:
            cv2.imwrite("scaled_image_1.25_0.75.jpg", scaled_image_1_25_0_75)
            print("Image saved successfully.")
        else:
            print("Please scale the image first.")
    elif choice == 'f':
        if original_image is not None:
            original_image = cv2.resize(original_image, (300, 300))
            print("Image resized to (300,300)")
            cv2.imshow("Resized Image (300x300)", original_image)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
        else:
            print("Please read an image first.")
    elif choice == 'x':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please select again.")
