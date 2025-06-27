frappe.listview_settings['Property'] = {
    onload: function(listview) {
        listview.page.add_menu_item('Mark as Vacant', function() {
            const selected = listview.get_checked_items().map(d => d.name);
            if(selected.length === 0) {
                frappe.msgprint("Please select at least one property.");
                return;
            }
            frappe.call({
                method: "rental_management.api.mark_properties_vacant",
                args: { property_names_json: JSON.stringify(selected) },
                callback: function(r) {
                    frappe.msgprint(r.message);
                    listview.refresh();
                }
            });
        });
    }
};
