# In apps/rental_management/rental_management/api.py

import frappe

# @frappe.whitelist() allows this function to be called from the frontend
@frappe.whitelist()
def get_monthly_payments_data():
    """Returns data for a bar chart of approved payments per month for the last 12 months."""
    approved_payments = frappe.db.sql(f"""
        SELECT
            SUM(amount) as total_amount,
            DATE_FORMAT(payment_date, '%%Y-%%m') as month
        FROM `tabPayments`
        WHERE status = 'Approved' AND payment_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
        GROUP BY month
        ORDER BY month ASC
    """, as_dict=True)

    if not approved_payments:
        return {"labels": [], "datasets": []}

    labels = [p.get('month') for p in approved_payments]
    data_points = [p.get('total_amount') for p in approved_payments]

    return {
        "labels": labels,
        "datasets": [{"name": "Monthly Payments", "values": data_points}]
    }