function getContactInfo(contactID) {
  return {
    name: document.getElementById("contactName-" + contactID).innerHTML,
    phone: document.getElementById("contactPhone-" + contactID).innerHTML,
    email: document.getElementById("contactEmail-" + contactID).innerHTML,
    job: document.getElementById("contactJob-" + contactID).innerHTML
  }
}

function displayContactInfo(contactID) {
  let contactInfo = getContactInfo(contactID);
  let contactPhone = "Phone Number: " + contactInfo.phone;
  let contactEmail = "Email: " + contactInfo.email;
  let contactJob = "Job Title & Company: " + contactInfo.job;

  document.getElementById("contactModalLabel").innerHTML = contactInfo.name;
  document.getElementById("contactModalPhone").innerHTML = contactPhone;
  document.getElementById("contactModalEmail").innerHTML = contactEmail;
  document.getElementById("contactModalJob").innerHTML = contactJob;

  document.getElementById("updateTrigger").addEventListener("click", prefillUpdateForm(contactID));
  document.getElementById("deleteButton").href = contactID;
}

function prefillUpdateForm(contactID) {
  let contactInfo = getContactInfo(contactID);

  document.getElementById("contact_id").value = contactID;
  document.getElementById("name").value = contactInfo.name;
  document.getElementById("job").value = contactInfo.job;
  document.getElementById("email").value = contactInfo.email;
  document.getElementById("phone").value = contactInfo.phone;
}