document.addEventListener('DOMContentLoaded', function () {
  // Format date and adjust time format
  document.querySelectorAll('.start-date-time').forEach(function (dateElement) {
    const dateString = dateElement.getAttribute('data-date');
    const date = new Date(dateString);

    // Format the date to the user's local time and preferred format
    const formattedDate = date.toLocaleString(navigator.language, {
      weekday: 'long', // Long weekday name
      year: 'numeric', // Full year
      month: 'short', // Short month name
      day: 'numeric', // Day of the month
      hour: '2-digit', // Hour (2 digits)
      minute: '2-digit', // Minute (2 digits)
      hour12: undefined, // Let browser decide between 12-hour or 24-hour format based on user locale
    });

    // Update the displayed date with the formatted one
    dateElement.textContent = formattedDate;
  });

  // Convert distance from meters to kilometers or miles depending on the user's locale
  document.querySelectorAll('.distance-value').forEach(function (distanceElement) {
    const distanceInMeters = parseFloat(distanceElement.getAttribute('data-distance'));

    // Determine the unit to use based on the user's locale
    const isUS = navigator.language === 'en-US';
    let distance;
    let unit;

    if (isUS) {
      // Convert to miles for US locale
      distance = distanceInMeters / 1609.344; // 1 mile = 1609.344 meters
      unit = 'mi';
    } else {
      // Convert to kilometers for other locales
      distance = distanceInMeters / 1000; // 1 kilometer = 1000 meters
      unit = 'km';
    }

    // Format the distance to 2 decimal places
    const formattedDistance = distance.toFixed(2);

    // Update the displayed distance with the formatted one
    distanceElement.textContent = `${formattedDistance} ${unit}`;
  });
});
