document.addEventListener('DOMContentLoaded', function () {
  // Format date and adjust time format
  document.querySelectorAll('.start-date-value').forEach(function (dateElement) {
    const dateString = dateElement.getAttribute('data-date');
    const date = new Date(dateString);

    // Format the date to the user's local time and preferred format
    const formattedDate = date.toLocaleString(navigator.language, {
      //weekday: 'long',
      year: 'numeric',
      month: 'numeric',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: undefined, // Let browser decide based on user locale
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
      distance = distanceInMeters / 1609.344;
      unit = 'mi';
    } else {
      distance = distanceInMeters / 1000;
      unit = 'km';
    }

    // Format to 2 decimal places
    const formattedDistance = distance.toFixed(2);

    // Update the displayed distance with the converted one
    distanceElement.textContent = `${formattedDistance} ${unit}`;
  });

  // Convert time from seconds to hours and minutes
  document.querySelectorAll('.moving-time-value').forEach(function (timeElement) {
    const time = timeElement.getAttribute('data-time');

    const hours = Math.floor(time / 3600);
    const minutes = Math.floor((time % 3600 % 60));

    // Update the displayed distance with the converted one
    timeElement.textContent = `${hours}h ${minutes}m`
  })
});
