# Import all necessary add-ons
from tkinter import *
import tkinter as tk
from tkmacosx import Button
from PIL import Image, ImageTk
import random
from tkinter import messagebox

# Define Cafe-Themes Colors with specific HexCodes
bg_c = "#E3DAC9"  # Bone, Dark Beige, WHITE SPACE OF THE GUI
txt_c1 = "#4A2D0D"  # Dark Brown, for Subheadings, and Main Texts
txt_c2 = "#000000"  # Black, for Body Texts, Normal

# Define Images

logo = "BiscottiLogo.png"
riccardo = "Riccardo.png"

product_images = {
    "Tea": "Tea.png",
    "Short Black Coffee": "Short Black Coffee.png",
    "Long Black Coffee": "Long Black Coffee.png",
    "Cappuccino": "Cappuccino.png",
    "Hot Chocolate": "Hot Chocolate.png",
    "Latte": "Latte.png"
}

extras_images = {"Extra Cream": "Extra Cream.png",
                 "Extra Chocolate": "Extra Chocolate.png"}

all_images = {"Tea": "Tea.png",
              "Short Black Coffee": "Short Black Coffee.png",
              "Long Black Coffee": "Long Black Coffee.png",
              "Cappuccino": "Cappuccino.png",
              "Hot Chocolate": "Hot Chocolate.png",
              "Latte": "Latte.png",
              "Extra Cream": "Extra Cream.png",
              "Extra Chocolate": "Extra Chocolate.png"
              }
# Define Prices

prices = {
    "Tea": "$2.00",
    "Short Black Coffee": "$3.50",
    "Long Black Coffee": "$4.00",
    "Cappuccino": "$4.50",
    "Hot Chocolate": "$4.00",
    "Latte": "$4.25",
    "Extra Cream": "$0.50",
    "Extra Chocolate": "$0.50"
}

# Historical Text

history = '''Welcome to Biscotti Cafe, a cherished establishment steeped in the rich traditions of Italian coffee culture. Founded in the picturesque streets of Italy by the visionary Riccardo Biscotti, our cafe is a testament to his unwavering passion for delivering an exceptional coffee experience. With a meticulous blend of artisanal brewing techniques and the finest hand-selected coffee beans, we invite you to indulge in the enchanting aroma and exquisite flavors that define our signature brews. At Biscotti Cafe, we strive to create a haven where every sip transports you to the vibrant streets of Italy, awakening your senses and leaving an indelible mark on your palate. Join us on this extraordinary journey as we celebrate the artistry, craftsmanship, and unmistakable charm of Italian coffee.'''

# Italian Quote

quote = '''Il caffè è il balsamo del cuore e dello spirito.'''

menu_items = {
    "Tea": "Experience the art of Tea with our exquisite selection of aromatic blends, providing a soothing and blissful experience.",
    "Short Black Coffee": "Indulge in the bold and robust flavours of our perfectly brewed Short Black Coffee.",
    "Long Black Coffee": "Savour the smooth and balanced taste of our meticulously crafted Long Black Coffee, delivering a Harmonious Blend of Strength and Aroma.",
    "Cappuccino - Biscotti's Choice": "Delight yourself in the creamy indulgence of  our expertly prepared Cappuccino, featuring a velvety blend of espresso and frothed milk.",
    "Hot Chocolate": "Immerse yourself  in the velvety decadence of our Hot Chocolate offering a premium blend of  premium cocoa.",
    "Latte - Consumer's Favourite": "Experience the perfect Harmony of  rich espresso and silky steamed milk in our signature Latte, creating a smooth and satisfying pleasing.",
    "Extra Cream/Chocolate": "Add our Signature Style Frothed Cream or our sought after Crunchy Chocolate Chips to make your experience blissful."
}


# Assign a Subroutine (Reusable code for further use) - ScreenSaver (Opening Window)


class BiscottiScreenSaver(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up the window
        self.title("Biscotti Screen Saver")
        self.geometry("900x750")
        self.configure(background=bg_c)
        self.resizable(False, False)

        # Image Resizing and Renaming

        # Now, Resized Logo is named as "logo_photo"
        logo_image = Image.open(logo)
        logo_image = logo_image.resize((245, 245), Image.BICUBIC)
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        # Now, Resized Image of 'Riccardo' is named as "riccardo_photo"
        riccardo_image = Image.open(riccardo)
        riccardo_image = riccardo_image.resize((245, 245), Image.BICUBIC)
        self.riccardo_photo = ImageTk.PhotoImage(riccardo_image)

        # Labels

        # Branding Message Label ("Biscotti Cafe")
        branding_label = tk.Label(self, text="Biscotti Cafe", font=("Zapfino", 40), fg=txt_c1, bg=bg_c)
        branding_label.place(relx=0.5, rely=0.15, anchor="center")

        # Historical Text Label
        history_label = tk.Label(self, text=history, font=("Times New Roman", 18), fg=txt_c2, bg=bg_c, wraplength=600,
                                 justify="center")
        history_label.place(relx=0.65, rely=0.45, anchor="center")

        # Italian Saying Label in Italic
        italiano_label = tk.Label(self, text=quote, font=("Times New Roman", 19, "italic"), fg=txt_c1, bg=bg_c,
                                  anchor="center")
        italiano_label.place(relx=0.65, rely=0.65, anchor="center")

        # Logo Image Label
        logo_label = tk.Label(self, image=self.logo_photo, bg=bg_c)
        logo_label.place(relx=0.15, rely=0.43, anchor="center")

        # Riccardo Image Label
        riccardo_label = tk.Label(self, image=self.riccardo_photo, bg=bg_c)
        riccardo_label.place(relx=0.19, rely=0.8, anchor="center")

        # Button that allows User to go to next Window
        experience_button = Button(self, text="Feel the Experience →", font=("Apple Chancery", 24, "bold"), fg=txt_c2,
                                   bg="#BBA793", padx=90, pady=20, command=self.show_biscotti_register)
        experience_button.place(relx=0.65, rely=0.80, anchor="center")

    def show_biscotti_register(self):
        # Hide the current window
        self.withdraw()

        # Create a new instance of Register
        register = BiscottiRegister()
        register.geometry("750x852")
        register.title("Biscotti POS")


# Assign a Subroutine (Reusable code for further use - Register (Where main functionalities of code will take place)


class BiscottiRegister(tk.Toplevel):
    product_quantities = {product: 0 for product in all_images}
    product_amounts = {product: 0 for product in all_images}
    total_daily_sales = 0

    def __init__(self):
        super().__init__()

        self.title("Biscotti POS")
        self.geometry("750x852")
        self.configure(bg=bg_c)
        self.resizable(False, False)

        # Overall Title with Separator, 10 spaces
        title_label = tk.Label(self, text="Biscotti Register - POS System          ",
                               font=("Zapfino", 30, "bold"), fg=txt_c1,
                               bg=bg_c)
        title_label.pack(pady=10)
        separator1 = tk.Frame(self, height=2, bg=txt_c1)
        separator1.pack(fill="x")

        quote_label = tk.Label(self, text=quote, font=("Times New Roman", 19, "italic", "bold"), bg=bg_c, fg=txt_c1)
        quote_label.place(relx=0.45, rely=0.94)

        logo_image = Image.open(logo)
        logo_image = logo_image.resize((105, 105), Image.BICUBIC)
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(title_label, image=self.logo_photo, bg=bg_c)
        logo_label.place(relx=0.82, rely=0.00004)

        # Customer Information Section
        customer_frame = tk.Frame(self, bg=bg_c)
        customer_frame.pack(padx=10, pady=10, anchor="w")

        # Customer Information Title
        customer_title_label = tk.Label(customer_frame, text="    Customer Information:                   ",
                                        font=("Apple Chancery", 18, "bold"), fg=txt_c1, bg=bg_c)
        customer_title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        separator2 = tk.Frame(self, height=2, bg=txt_c1)
        separator2.pack(fill="x")

        # Customer Name
        name_label = tk.Label(customer_frame, text="Name:", font=("Times New Roman", 12), fg=txt_c2, bg=bg_c)
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Updated grid position
        name_entry = tk.Entry(customer_frame, font=("Times New Roman", 12), width=15)
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")  # Updated grid position

        # Order Number

        def generate_order_number():
            return random.randint(100, 999)

        order_number_label = tk.Label(customer_frame, text="Order No:", font=("Times New Roman", 12), fg=txt_c2,
                                      bg=bg_c)
        order_number_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")  # Updated grid position
        order_number_value = tk.IntVar()
        order_number_value.set(generate_order_number())
        order_number_entry = tk.Entry(customer_frame, font=("Times New Roman", 12), textvariable=order_number_value,
                                      state="readonly", width=8)
        order_number_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")  # Updated grid position

        # Separator between Customer Information and Title
        separator3 = tk.Frame(self, width=2, bg=txt_c1)
        separator3.place(relx=0.355, rely=0.2289, relheight=100)

        # Products Frame
        products_frame = tk.Frame(self, bg=bg_c)
        products_frame.pack(pady=10, anchor="w")

        # Extras Frame
        extras_frame = tk.Frame(self, bg=bg_c)
        extras_frame.pack(pady=10, anchor="w")

        # Order Frame
        order_frame = Frame(self, bg=bg_c)
        order_frame.place(relx=0.4, rely=0.3)

        order_scrollbar = Scrollbar(order_frame, orient=VERTICAL)

        # Product Section Title
        products_title_label = tk.Label(products_frame, text="Beverages",
                                        font=("Apple Chancery", 18, "bold", "underline"),
                                        fg=txt_c1, bg=bg_c)
        products_title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Create a dictionary to store the product labels
        product_labels = {}

        # Create product labels and images in 3x2 grid
        row, col = 1, 0
        for product, img_file in product_images.items():
            img = Image.open(img_file)
            img = img.resize((80, 80), Image.BICUBIC)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(products_frame, image=photo, text=product, compound="top",
                             font=("Times New Roman", 12, "bold"), fg=txt_c2, bg=bg_c)
            label.image = photo
            label.grid(row=row, column=col, padx=15, pady=5, sticky="nsew")  # Use grid manager
            product_labels[product] = label
            col += 1
            if col > 1:
                col = 0
                row += 1

        row, col = row + 1, 0
        for extra, img_file in extras_images.items():
            img = Image.open(img_file)
            img = img.resize((80, 80), Image.BICUBIC)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(extras_frame, image=photo, text=extra, compound="top",
                             font=("Times New Roman", 15, "bold"), fg=txt_c2, bg=bg_c)
            label.image = photo
            label.grid(row=row, column=col, padx=15.9, pady=5, sticky="nsew")  # Reduce padx value
            product_labels[extra] = label
            col += 1
            if col > 1:
                col = 0
                row += 1

        # Extras Section Title
        extras_title_label = tk.Label(extras_frame, text="Extras", font=("Apple Chancery", 18, "bold", "underline"),
                                      fg=txt_c1,
                                      bg=bg_c)
        extras_title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Create Title
        order_title_label = tk.Label(self, text="Order", font=("Apple Chancery", 20, "bold", "underline"),
                                     fg=txt_c1,
                                     bg=bg_c)
        order_title_label.place(relx=0.638, rely=0.25)

        # Create a listbox for the order items
        order_listbox = Listbox(order_frame, font=("Times New Roman", 15), height=13, width=52,
                                yscrollcommand=order_scrollbar.set)
        order_scrollbar.config(command=order_listbox.yview)
        order_scrollbar.pack(side=RIGHT, fill="y")
        order_listbox.pack(pady=1, fill=tk.BOTH, expand=True)

        # Horizontal Separator between Order Listbox and Total Label
        separator5 = tk.Frame(self, width=490, height=2, bg=txt_c1)
        separator5.place(relx=0.683, rely=0.6, anchor="center")

        # Add to Order Function
        total = 0

        def add_to_order(item):
            nonlocal total
            price = prices.get(item, "$0.00")
            order_listbox.insert(tk.END, f"{item} - {price}")
            order_listbox.insert(tk.END, "")  # Empty line for spacing
            total += float(price.replace('$', ''))
            total_label.config(text=f"Total: ${total:.2f}")

        def delete():
            nonlocal total
            selected_item = order_listbox.curselection()
            if selected_item:
                item = order_listbox.get(selected_item[0])
                price = item.split(" - ")[1]  # Extract the price from the item string
                total -= float(price.replace('$', ''))
                order_listbox.delete(selected_item[0])
                total_label.config(text=f"Total: ${total:.2f}")

        # Bind the click event to add the item to the order list
        for product in product_labels:
            product_labels[product].bind("<Button-1>", lambda event, p=product: add_to_order(p))

        # Total Label
        total_label = tk.Label(self, text="Total: $0.00", font=("Times New Roman", 30, "bold"), fg=txt_c1, bg=bg_c)
        total_label.place(relx=0.38, rely=0.62)

        # Pay Button
        def pay():
            nonlocal total

            # Collect information about products sold and their prices
            order_list = order_listbox.get(0, tk.END)

            # Update the quantities and amounts based on the current order
            for PRODUCTEXTRA in all_images:
                quantity = order_list.count(f"{PRODUCTEXTRA} - {prices[PRODUCTEXTRA]}")
                BiscottiRegister.product_quantities[PRODUCTEXTRA] += quantity
                BiscottiRegister.product_amounts[PRODUCTEXTRA] += quantity * float(
                    prices[PRODUCTEXTRA].replace('$', ''))

            # Calculate the total daily sales
            BiscottiRegister.total_daily_sales = sum(BiscottiRegister.product_amounts.values())

            # Write the updated order information to the file
            with open('data_sales.txt', 'w') as file:
                order_info_lines = ["Total Number of Products Sold:"]
                for PRODUCTEXTRA, quantity in BiscottiRegister.product_quantities.items():
                    order_info_lines.append(f"{PRODUCTEXTRA}: {quantity}")
                order_info_lines.append("")

                order_info_lines.append("Total Amount of Money Made on Each Product:")
                for PRODUCTEXTRA, amount in BiscottiRegister.product_amounts.items():
                    order_info_lines.append(f"{PRODUCTEXTRA}: ${amount:.2f}")
                order_info_lines.append("")

                order_info_lines.append(
                    f"Total Amount of Money Made in Total: ${BiscottiRegister.total_daily_sales:.2f}")

                file.write('\n'.join(order_info_lines))

            order_listbox.delete(0, tk.END)
            total_label.config(text="Total: $0.00")
            total = 0

            def generate_ordernumber():
                return random.randint(100, 999)

            order_numberlabel = tk.Label(customer_frame, text="Order No:", font=("Times New Roman", 12), fg=txt_c2,
                                         bg=bg_c)
            order_numberlabel.grid(row=0, column=2, padx=5, pady=5, sticky="e")  # Updated grid position
            order_numbervalue = tk.IntVar()
            order_numbervalue.set(generate_ordernumber())
            order_numberentry = tk.Entry(customer_frame, font=("Times New Roman", 12), textvariable=order_numbervalue,
                                         state="readonly", width=8)
            order_numberentry.grid(row=0, column=3, padx=5, pady=5, sticky="w")  # Updated grid position

            # Customer Name
            namelabel = tk.Label(customer_frame, text="Name:", font=("Times New Roman", 12), fg=txt_c2, bg=bg_c)
            namelabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Updated grid position
            nameentry = tk.Entry(customer_frame, font=("Times New Roman", 12), width=15)
            nameentry.grid(row=0, column=1, padx=5, pady=5, sticky="w")  # Updated grid position

        def reset():
            # Reset the product quantities and amounts to 0
            for product in BiscottiRegister.product_quantities:
                BiscottiRegister.product_quantities[product] = 0
                BiscottiRegister.product_amounts[product] = 0

            # Reset the total daily sales to 0
            BiscottiRegister.total_daily_sales = 0
            with open('data_sales.txt', 'w') as file:
                file.write('')
            messagebox.showinfo("Data Sales Reset", "The Sales File has been reset.", icon="info")

        pay_button = Button(self, text="Paid Cash/Card ✓", font=("Times New Roman", 17, "bold"), fg=txt_c2,
                            bg="#228B22", padx=20, pady=10, command=pay, height=65, width=250)
        pay_button.place(relx=0.63, rely=0.6065)

        separator6 = tk.Frame(self, width=2000, height=2, bg=txt_c1)
        separator6.place(relx=0.683, rely=0.6901, anchor="center")

        separator7 = tk.Frame(self, width=490, height=2, bg=txt_c1)
        separator7.place(relx=0.03, rely=0.9, anchor="center")

        remove_product_button = Button(self, text="Remove Item ✗", font=("Times New Roman", 17, "bold"), fg=txt_c2,
                                       bg="#B22222", height=64, width=240, command=delete)
        remove_product_button.place(relx=0.019, rely=0.91)

        description_button = Button(self, text="View Descriptions", font=("Times New Roman", 17, "bold"), fg=txt_c2,
                                    bg="white", height=64, width=200, command=self.show_menu)
        description_button.place(relx=0.4, rely=0.73)

        screensaver_button = Button(self, text="Screen Saver", font=("Times New Roman", 17, "bold"), fg=txt_c2,
                                    bg="white", height=64, width=200, command=BiscottiScreenSaver)

        screensaver_button.place(relx=0.7, rely=0.73)

        reset_sales_button = Button(self, text="Reset Sales for Day ↻", font=("Times New Roman", 17, "bold"), fg=txt_c2,
                                    bg="white", height=64, width=400, command=reset)

        reset_sales_button.place(relx=0.41, rely=0.85)

    def show_menu(self):

        # Create a new instance of FullMenu
        menu = Menu(self)
        menu.geometry("450x850")

        menu.mainloop()


class Menu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        # Setting up the window
        self.title("Item Descriptions")
        self.geometry("450x850")
        self.configure(background=bg_c)
        self.resizable(False, False)

        descriptions = "Descriptions.png"
        descriptions_image = Image.open(descriptions)
        descriptions_image = descriptions_image.resize((450, 800), Image.BICUBIC)
        self.descriptions_photo = ImageTk.PhotoImage(descriptions_image)

        descriptions_label = tk.Label(self, image=self.descriptions_photo, bg=bg_c)
        descriptions_label.pack()

        to_register_from_description = tk.Button(self, text="Return to Register", font=("Times New Roman", 17, "bold"),
                                                 bg=bg_c, height=2, width=20, command=self.destroy)
        to_register_from_description.place(relx=0.27, rely=0.92)


if __name__ == "__main__":
    app = BiscottiScreenSaver()
    app.mainloop()

