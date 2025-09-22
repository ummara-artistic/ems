# Labor Management System

A comprehensive Django-based labor management system designed for managing employees, attendance, and salary calculations with bilingual support (English/Urdu).

## Features

### 🔐 Authentication
- Hardcoded admin login (username: `admin`, password: `admin`)
- Secure session management
- Professional login interface

### 👥 Employee Management
- Add, edit, delete employees
- Employee types: Labor Workers & Office Employees
- Search and filter functionality
- Modal-based forms for quick operations
- Employee profile management

### 📅 Attendance Management
- Daily attendance marking with in/out times
- Overtime tracking and calculation
- Monthly attendance reports with calendar view
- Bulk attendance operations
- Attendance statistics and analytics

### 💰 Salary Management
- Automated salary calculation based on attendance
- Overtime compensation (1.5x rate)
- Tea allowance and deductions management
- Dues tracking (positive/negative balances)
- Monthly salary generation and editing

### 📄 PDF Generation
- Bilingual salary slips (English/Urdu)
- Professional PDF layout
- Downloadable salary reports
- Detailed calculation breakdowns
- Company branding support

### 📊 Dashboard & Analytics
- Real-time statistics and KPIs
- Attendance trends and charts
- Employee distribution analytics
- Top performers tracking
- Monthly summaries and reports

## Installation

### Prerequisites
- Python 3.8+
- Django 4.2+
- ReportLab (for PDF generation)

### Setup Instructions

1. **Install Dependencies**
   \`\`\`bash
   python scripts/install_dependencies.py
   \`\`\`

2. **Setup Database**
   \`\`\`bash
   python scripts/setup_database.py
   \`\`\`

3. **Create Sample Data (Optional)**
   \`\`\`bash
   python scripts/create_sample_data.py
   \`\`\`

4. **Run the Server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

5. **Access the System**
   - URL: `http://localhost:8000`
   - Username: `admin`
   - Password: `admin`

## System Architecture

### Models
- **Employee**: Core employee information and details
- **Attendance**: Daily attendance records with overtime
- **SalaryRecord**: Monthly salary calculations and payments

### Key Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Professional UI**: Clean, modern interface with Bootstrap
- **Bilingual Support**: English and Urdu text in PDFs
- **Real-time Updates**: Live calculations and statistics
- **Data Validation**: Comprehensive form validation
- **Search & Filter**: Advanced filtering across all modules

### Salary Calculation Logic
- **Basic Salary**: Proportional to working days and attendance
- **Overtime**: 1.5x hourly rate for extra hours
- **Tea Allowance**: Fixed Rs. 1000 monthly allowance
- **Deductions**: Automatic deduction for absent days
- **Dues**: Flexible positive/negative balance tracking

### PDF Features
- **Bilingual Layout**: English and Urdu side-by-side
- **Professional Design**: Clean, printable format
- **Detailed Breakdown**: Complete salary calculation details
- **Company Branding**: Customizable header and footer
- **Download Support**: Direct PDF download functionality

## Usage Guide

### Adding Employees
1. Navigate to Employees section
2. Click "Add Employee" button
3. Fill in required details (name, age, salary, type)
4. Save to create employee record

### Marking Attendance
1. Go to Attendance section
2. Click "Mark Attendance"
3. Select employee, date, and status
4. Add in/out times and overtime if applicable
5. Save attendance record

### Generating Salaries
1. Access Salary Management
2. Select employee from dropdown
3. Choose month/year for calculation
4. Review auto-calculated amounts
5. Adjust dues or deductions if needed
6. Generate salary record

### Downloading PDF Salary Slips
1. Go to salary records list
2. Click PDF icon next to any record
3. PDF will download automatically
4. Contains bilingual salary details

## Customization

### Adding New Fields
- Modify models in respective apps
- Update forms and templates
- Run migrations to apply changes

### Changing Calculation Logic
- Edit salary calculation in `salary/views.py`
- Modify overtime rates and allowances
- Update PDF generation accordingly

### Styling Customization
- Edit CSS variables in `base.html`
- Modify Bootstrap classes
- Add custom styling as needed

## Support

For technical support or feature requests, please refer to the system documentation or contact the development team.

## License

This project is developed for internal use and follows standard Django practices and security guidelines.
