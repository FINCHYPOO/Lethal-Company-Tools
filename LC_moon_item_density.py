import tkinter as tk
from tkinter import messagebox


lethal_company_moons = {
    'Experimentation': {'Risk Level': 'B', 'Cost (c)': 0, 'Default Layout': 'Factory', 'Map Size Multiplier': 1, 'Min Scrap': 8, 'Max Scrap': 11, 'Max Indoor Power': 4, 'Max Nighttime power': 8, 'Viable Weather': ['Rainy', 'Stormy', 'Foggy', 'Flooded', 'Eclipsed']},
    'Assurance': {'Risk Level': 'D', 'Cost (c)': 0, 'Default Layout': 'Factory', 'Map Size Multiplier': 1, 'Min Scrap': 13, 'Max Scrap': 16, 'Max Indoor Power': 6, 'Max Nighttime power': 8, 'Viable Weather': ['Rainy', 'Stormy', 'Flooded', 'Eclipsed']},
    'Vow': {'Risk Level': 'C', 'Cost (c)': 0, 'Default Layout': 'Factory', 'Map Size Multiplier': 1.15, 'Min Scrap': 10, 'Max Scrap': 12, 'Max Indoor Power': 7, 'Max Nighttime power': 6, 'Viable Weather': ['Flooded', 'Stormy', 'Foggy', 'Eclipsed']},
    'Offense': {'Risk Level': 'B', 'Cost (c)': 0, 'Default Layout': 'Factory', 'Map Size Multiplier': 1.25, 'Min Scrap': 14, 'Max Scrap': 17, 'Max Indoor Power': 12, 'Max Nighttime power': 8, 'Viable Weather': ['Rainy', 'Stormy', 'Eclipsed', 'Flooded']},
    'March': {'Risk Level': 'B', 'Cost (c)': 0, 'Default Layout': 'Factory', 'Map Size Multiplier': 2, 'Min Scrap': 13, 'Max Scrap': 16, 'Max Indoor Power': 14, 'Max Nighttime power': 12, 'Viable Weather': ['Flooded', 'Stormy', 'Foggy', 'Eclipsed']},
    'Rend': {'Risk Level': 'A', 'Cost (c)': 550, 'Default Layout': 'Mansion', 'Map Size Multiplier': 1.2, 'Min Scrap': 18, 'Max Scrap': 25, 'Max Indoor Power': 10, 'Max Nighttime power': 6, 'Viable Weather': ['Stormy', 'Eclipsed']},
    'Dine': {'Risk Level': 'S', 'Cost (c)': 600, 'Default Layout': 'Mansion', 'Map Size Multiplier': 1.3, 'Min Scrap': 20, 'Max Scrap': 27, 'Max Indoor Power': 15, 'Max Nighttime power': 6, 'Viable Weather': ['Flooded', 'Eclipsed']},
    'Titan': {'Risk Level': 'S+', 'Cost (c)': 700, 'Default Layout': 'Factory', 'Map Size Multiplier': 2.35, 'Min Scrap': 23, 'Max Scrap': 37, 'Max Indoor Power': 18, 'Max Nighttime power': 7, 'Viable Weather': ['Stormy', 'Foggy', 'Eclipsed']},
}


def on_submit():
    selected_moon = selected_moon_var.get()

    try:
        min_loot = lethal_company_moons[selected_moon]['Min Scrap']
        loot_density = lethal_company_moons[selected_moon]['Min Scrap'] / lethal_company_moons[selected_moon]['Map Size Multiplier']

        result_text.set(f"The minimum loot for {selected_moon} is: {min_loot}\n"
                        f"The loot density for {selected_moon} is: {loot_density}")
    except KeyError:
        result_text.set(f"Error: Moon data not available for {selected_moon}")
        messagebox.showerror("Error", f"Error: Moon data not available for {selected_moon}")

# GUI setup
root = tk.Tk()
root.title("Lethal Company Moon Lookup")

def create_gui():
    # Dropdown menu for moon selection
    moon_label = tk.Label(root, text="Select a moon:")
    moon_label.pack()

    # Description labels
    description_label = tk.Label(root, text="Descriptions:")
    description_label.pack()

    min_loot_description = tk.Label(root,
                                    text="Minimum Loot: The minimum amount of loot that can be obtained on the specified moon.")
    min_loot_description.pack()

    item_density_description = tk.Label(root,
                                        text="Item Density: Calculated by dividing the minimum loot by the map size multiplier, providing a measure of loot concentration.")
    item_density_description.pack()

    map_size_multiplier_description = tk.Label(root,
                                               text="Map Size Multiplier: A factor that determines the moon's map size.")
    map_size_multiplier_description.pack()

    global selected_moon_var
    selected_moon_var = tk.StringVar()
    selected_moon_var.set(list(lethal_company_moons.keys())[0])  # Set default moon
    moon_dropdown = tk.OptionMenu(root, selected_moon_var, *lethal_company_moons.keys())
    moon_dropdown.pack()

    # Button to trigger the moon lookup
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    # Display the result
    global result_text
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text)
    result_label.pack()

# Run the GUI
create_gui()
root.mainloop()