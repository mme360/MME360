def execute(filters=None):
    columns = [
        {"label": "Incident", "fieldname": "name", "fieldtype": "Link", "options": "Support Incident", "width": 180},
        {"label": "Title", "fieldname": "incident_title", "fieldtype": "Data", "width": 220},
        {"label": "Analyzer", "fieldname": "analyzer", "fieldtype": "Link", "options": "Analyzer", "width": 180},
        {"label": "Severity", "fieldname": "severity", "fieldtype": "Data", "width": 120},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": "Reported On", "fieldname": "reported_on", "fieldtype": "Datetime", "width": 180}
    ]
    data = []
    return columns, data
