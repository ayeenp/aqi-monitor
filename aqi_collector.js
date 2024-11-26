const { GLib } = imports.gi;

const filePath = '/tmp/aqi-collector/last_aqi.txt';

function getAQI() {
    try {
        if (!GLib.file_test(filePath, GLib.FileTest.EXISTS)) {
            log('Error: AQI file does not exist.');
            return null;
        }

        let [ok, content] = GLib.file_get_contents(filePath);

        if (!ok) {
            log('Error: Failed to read AQI file.');
            return null;
        }

        const contentStr = content.toString().trim();
        const aqiValueStr = contentStr.split('|')[0];
        const aqiValue = parseInt(aqiValueStr, 10);

        // Validate that the value is a number
        if (isNaN(aqiValue)) {
            log('Error: AQI file does not contain a valid integer.');
            return null;
        }

        return aqiValue;
    } catch (error) {
        log(`Error reading AQI from file: ${error}`);
        return null;
    }
}

var AQICollector = {
    getAQI,
};
