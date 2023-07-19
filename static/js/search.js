// document.addEventListener('DOMContentLoaded', function() {
//     // Move the searchUsers() function here from your previous script
//     function searchUsers() {
//         const searchInput = document.getElementById('searchInput');
        
//         if (!searchInput) {
//             console.error('searchInput element not found.');
//             return;
//         }
    
//         const inputValue = searchInput.value.trim();
        
//         if (inputValue === '') {
//             console.warn('Search input is empty.');
//             return;
//         }
    
//         const url = `/search/?username=${encodeURIComponent(inputValue)}`;
    
//         fetch(url)
//             .then(response => response.json())
//             .then(data => {
//                 const userList = document.getElementById('userList');
//                 userList.innerHTML = '';
    
//                 if (data.length === 0) {
//                     userList.innerHTML = '<p>No users found.</p>';
//                 } else {
//                     data.forEach(user => {
//                         const userSection = document.createElement('section');
//                         userSection.innerHTML = `
//                             <p style="text-align: left; margin-left: 15px; color: aliceblue;">Name: ${user.username}</p>
//                             <p style="text-align: left; margin-left: 15px; color: aliceblue;">Email: ${user.email}</p>
//                             <button class="button-3d">Chat</button>
//                         `;
//                         userList.appendChild(userSection);
//                     });
//                 }
//             })
//             .catch(error => console.error('Error fetching user data:', error));
//     }
    
//     // Add event listener to the button with id="searchButton"
//     document.getElementById('searchButton').addEventListener('click', searchUsers);
// });