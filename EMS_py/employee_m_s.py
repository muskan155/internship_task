from datetime import datetime  # python ko built-in 'datetime' module bata 'datetime' class lai import gareko

class Employee:  # class lai define gareko
    def __init__(self, name, emp_id): #init method le employee lai initialize gareko
        self.name = name       # initialized employee along with name
        self.emp_id = emp_id   # initialized employee along with id
        self.start_time = None # initialized start_time as none
        self.end_time = None   # initialized end_time with none

    def clock_in(self, start_time): # clock_in method sets the 'start_time' employee ko lagi
        self.start_time = datetime.strptime(start_time, '%H:%M') # start_time vanne string lai datatime object with format '%H:%M'ma lagna lai 'datetime.strptime' use gareko

    def clock_out(self, end_time):  # clock_out method sets the 'end_time' employee ko lagi
        self.end_time = datetime.strptime(end_time, '%H:%M')   # end_time vanne string lai datatime object with format '%H:%M'ma lagna lai 'datetime.strptime' use gareko

    def working_status(self):  # working_status method le employee ko work session calculate garera status return garcha
        if self.start_time is None or self.end_time is None:  # it first checks start_time or end_time is None, indicating incomplete data.
            return "Incomplete clock-in/out data"

        # Define the standard times
        early_start_time = datetime.strptime("08:45", '%H:%M')
        late_start_time = datetime.strptime("09:00", '%H:%M')
        standard_end_time = datetime.strptime("05:00", '%H:%M')

        # Check start status
        if early_start_time <= self.start_time <= late_start_time:
            start_status = "In time"
        else:
            start_status = "Delayed"

        # Calculate working hours
        total_worked = self.end_time - self.start_time
        hours_worked = total_worked.total_seconds() / 3600  # Convert seconds to hours

        # Check if overtime and calculate extra hours
        if self.end_time > standard_end_time:
            overtime_duration = self.end_time - standard_end_time
            overtime_hours = overtime_duration.seconds // 3600
            overtime_minutes = (overtime_duration.seconds % 3600) // 60
            overtime_status = f"Overtime (extra {overtime_hours} hours and {overtime_minutes} minutes)"
        else:
            overtime_status = "Normal hours"

        return {  # return statement le dictionary return garcha jasko key-value pairs huncha.
            "Employee ID": self.emp_id,
            "Name": self.name,
            "Start Time": self.start_time.strftime('%H:%M'),
            "End Time": self.end_time.strftime('%H:%M'),
            "Start Status": start_status,
            "Total Hours Worked": round(hours_worked, 2),
            "Overtime Status": overtime_status
        }

# Function to take user input and create an employee
def main():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    employee = Employee(name, emp_id)

    start_time = input("Enter start time (HH:MM): ")
    employee.clock_in(start_time)

    end_time = input("Enter end time (HH:MM): ")
    employee.clock_out(end_time)

    status = employee.working_status()
    print("\nEmployee Work Status:")
    for key, value in status.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()