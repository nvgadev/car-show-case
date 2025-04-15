fetch('/api/cars')
  .then(response => response.json())
  .then(cars => {
    const carList = document.getElementById('car-list');
    cars.forEach(car => {
      const card = document.createElement('div');
      card.className = 'car-card';
      card.innerHTML = `
        <img src="${car.image}" alt="${car.model}" />
        <h2>${car.model}</h2>
        <p>${car.description}</p>
        <ul>
          ${car.technologies.map(tech => `<li>${tech}</li>`).join('')}
        </ul>
      `;
      carList.appendChild(card);
    });
  })
  .catch(error => console.error('Error fetching car data:', error));
