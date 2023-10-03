import tkinter as tk
import matplotlib
import sys

matplotlib.use("TkAgg")


# Define function to open the main window
def open_main_window():
    # Import necessary libraries
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    # Define the calculation function
    def calculate():
        puffs = int(puffs_entry.get())
        tank_size = float(tank_size_entry.get())
        bottle_size = float(bottle_size_entry.get())
        nicotine_strength = float(nicotine_strength_entry.get())

        nicotine_intake = (puffs * tank_size * nicotine_strength) / bottle_size / 1000
        output_label.config(text=f"Nicotine intake: {nicotine_intake:.2f} mg")
        with open('nicotineingestion.txt', 'a') as f:
            f.write(f"{nicotine_intake:.2f}\n")

    # Define the plot function
    def plot():
        with open('nicotineingestion.txt', 'r') as f:
            data = f.readlines()
            data = [float(d.strip()) for d in data]
        fig, ax = plt.subplots()
        ax.plot(data, color='blue')
        ax.scatter(range(len(data)), data, color='red', marker='x')

        # Set xticks and xticklabels
        xticks = range(0, len(data), 1)  # Change 5 to set the desired interval
        xticklabels = range(1, len(xticks) + 1)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels)

        ax.set_xlabel('Days')
        ax.set_ylabel('Nicotine intake (mg)')

        # Embed the plot into a Tkinter canvas
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        ax.tick_params(width=2)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def clear_plot():
        puffs_entry.delete(0, tk.END)
        tank_size_entry.delete(0, tk.END)
        bottle_size_entry.delete(0, tk.END)
        nicotine_strength_entry.delete(0, tk.END)
        output_label.config(text="")
        with open('nicotineingestion.txt', 'w') as f:
            pass

    # Create the main window
    window = tk.Tk()
    window.title("Vape Nicotine Tracker")

    # Create the input widgets
    puffs_label = tk.Label(window, text="Enter daily puffs:")
    puffs_label.pack()
    puffs_entry = tk.Entry(window)
    puffs_entry.pack()

    tank_size_label = tk.Label(window, text="Enter tank size (in ml):")
    tank_size_label.pack()
    tank_size_entry = tk.Entry(window)
    tank_size_entry.pack()

    bottle_size_label = tk.Label(window, text="Enter bottle size (in ml):")
    bottle_size_label.pack()
    bottle_size_entry = tk.Entry(window)
    bottle_size_entry.pack()

    nicotine_strength_label = tk.Label(window, text="Enter nicotine strength (in mg/ml):")
    nicotine_strength_label.pack()
    nicotine_strength_entry = tk.Entry(window)
    nicotine_strength_entry.pack()

    calculate_button = tk.Button(window, text="Calculate", command=calculate)
    calculate_button.pack()

    # Create the output label widget
    output_label = tk.Label(window, text="")
    output_label.pack()

    # Create the disclaimer text widget
    disclaimer_text = "DISCLAIMER: This calculation is an estimate and may not reflect the actual amount of nicotine " \
                      "that is absorbed by the body. Nicotine intake can vary based on individual factors such as " \
                      "inhalation technique, lung capacity, and nicotine metabolism rate. This tool is intended for " \
                      "informational purposes only and should not be used as a substitute for medical advice."
    disclaimer = tk.Text(window, height=6, wrap=tk.WORD)
    disclaimer.pack()
    disclaimer.insert(tk.END, disclaimer_text)
    disclaimer.config(state=tk.DISABLED)

    # Create the plot button
    plot_button = tk.Button(window, text="Plot", command=plot)
    plot_button.pack()

    # Creates the clear button
    clear_button = tk.Button(window, text="Clear Plots", command=clear_plot)
    clear_button.pack()

    # Start the main event loop
    window.mainloop()

    plt.close('all')


# Create the home screen
home_screen = tk.Tk()
home_screen.title("Vape Nicotine Tracker")

# Create the buttons
open_button = tk.Button(home_screen, text="Open Vape Nicotine Tracker", command=open_main_window)
open_button.pack(pady=20)

exit_button = tk.Button(home_screen, text="Exit", command=lambda: sys.exit(0))
exit_button.pack(pady=10)

home_screen.mainloop()
