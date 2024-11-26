const { St, Clutter, GLib } = imports.gi;
const Main = imports.ui.main;
const AQICollector = imports.misc.extensionUtils.getCurrentExtension().imports.aqi_collector.AQICollector;

let button;
let timeoutId;

function init() {
    log("AQI Monitor extension initialized");
}

function enable() {
    log("Enabling AQI Monitor extension");

    button = new St.Button({
        style_class: 'panel-button',
        reactive: true,
        can_focus: true,
        track_hover: true,
    });

    let label = new St.Label({
        y_align: Clutter.ActorAlign.CENTER,
    });

    let aqiValue = AQICollector.getAQI();

    if (aqiValue === null) {
        label.set_text('-1');
    }
    else {
        label.set_text(aqiValue.toString());
    }

    button.set_child(label);

    Main.panel._rightBox.insert_child_at_index(button, 0);

    timeoutId = GLib.timeout_add(GLib.PRIORITY_DEFAULT, 2 * 60 * 1000, () => {
        let aqiValue = AQICollector.getAQI();

        if (aqiValue === null) {
            label.set_text('-1');
        }
        else {
            label.set_text(aqiValue.toString());
        }
        
        return true; // Keep the timer running
    });
}

function disable() {
    log("Disabling AQI Monitor extension");

    // Remove the timer
    if (timeoutId) {
        GLib.Source.remove(timeoutId);
        timeoutId = null;
    }

    // Remove the button
    if (button) {
        Main.panel._rightBox.remove_child(button);
        button.destroy();
        button = null;
    }
}
