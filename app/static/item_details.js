
document.addEventListener('DOMContentLoaded', () => {
  const updateForm = document.getElementById('update-item-form');
  const deleteForm = document.getElementById('delete-item-form');

  async function submitForm(event) {
      event.preventDefault();

      const form = event.target;
      const method = form.dataset.method;
      const url = form.dataset.url;
      const formData = new FormData(form);
      const data = Object.fromEntries(formData.entries());

      const response = await fetch(url, {
          method: method,
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
      });

      if (response.ok) {
          window.location.href = indexURL; // use the global variable defined in the template
      } else {
          const error = await response.json();
          alert(`error: ${error.error}`);
      }
  }

  if (updateForm) {
      updateForm.addEventListener('submit', submitForm);
  }

  if (deleteForm) {
      deleteForm.addEventListener('submit', submitForm);
  }
});
