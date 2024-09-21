
document.addEventListener('DOMContentLoaded', function() {
    const resumeForm = document.getElementById('resume-form');
    const displayResume = document.getElementById('display-resume');
  
    resumeForm.addEventListener('submit', function(event) {
      event.preventDefault();

      const fullName = document.getElementById('fullName').value;
      const address = document.getElementById('address').value;
      const mobile = document.getElementById('mobile').value;
      const email = document.getElementById('email').value;
      const hobbies = document.getElementById('hobbies').value;
  
      const eduItems = document.querySelectorAll('.edu-item');
      const eduQualifications = [];
      eduItems.forEach(function(eduItem) {
        const degree = eduItem.querySelector('.eduDegree').value;
        const university = eduItem.querySelector('.eduUniversity').value;
        const year = eduItem.querySelector('.eduYear').value;
        eduQualifications.push({ degree, university, year });
      });

  
      const certificationItems = document.querySelectorAll('.certification-item');
      const certifications = [];
      certificationItems.forEach(function(certificationItem) {
        const title = certificationItem.querySelector('.certificationTitle').value;
        const organization = certificationItem.querySelector('.certificationOrganization').value;
        const year = certificationItem.querySelector('.certificationYear').value;
        certifications.push({ title, organization, year });
      });
  
      const experienceItems = document.querySelectorAll('.experience-item');
      const experiences = [];
      experienceItems.forEach(function(experienceItem) {
        const title = experienceItem.querySelector('.experienceTitle').value;
        const organization = experienceItem.querySelector('.experienceOrganization').value;
        const duration = experienceItem.querySelector('.experienceDuration').value;
        experiences.push({ title, organization, duration });
      });

      const skills = [];
      const skillInputs = document.querySelectorAll('.skill');
      skillInputs.forEach(function(skillInput) {
        skills.push(skillInput.value);
      });
  
      const photo = document.getElementById('photo').files[0];

      displayResume.style.display = 'block';
      displayResume.innerHTML = `
        <h1>${fullName}</h1>
        <p><strong>Address:</strong> ${address}</p>
        <p><strong>Mobile No:</strong> ${mobile}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Hobbies:</strong> ${hobbies}</p>
        <h2>Educational Qualifications</h2>
        ${eduQualifications.map(edu => `
          <p><strong>Degree:</strong> ${edu.degree}</p>
          <p><strong>University:</strong> ${edu.university}</p>
          <p><strong>Graduation Year:</strong> ${edu.year}</p>
        `).join('')}
       
        <h2>Certifications/Awards</h2>
        ${certifications.map(certification => `
          <p><strong>Title:</strong> ${certification.title}</p>
          <p><strong>Organization:</strong> ${certification.organization}</p>
          <p><strong>Year:</strong> ${certification.year}</p>
        `).join('')}
        <h2>Experience</h2>
        ${experiences.map(experience => `
          <p><strong>Title:</strong> ${experience.title}</p>
          <p><strong>Organization:</strong> ${experience.organization}</p>
          <p><strong>Duration:</strong> ${experience.duration}</p>
        `).join('')}
        <h2>Skills</h2>
        ${skills.map(skill => `<p>${skill}</p>`).join('')}
        <img id="resume-photo" alt="Your Photo">
      `;

      const resumePhoto = document.getElementById('resume-photo');
      if (photo) {
        resumePhoto.src = URL.createObjectURL(photo);
      }
    });
});



