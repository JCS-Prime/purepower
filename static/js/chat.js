// Toggle chat open/close
function toggleChat() {
    const chatBox = document.getElementById("chatBox");
    chatBox.classList.toggle("open");
}

// Send message
async function sendMessage() {
    const input = document.getElementById("userInput");
    const messages = document.getElementById("chatMessages");
    const userText = input.value.trim();

    if (!userText) return;

    // Show user message
    messages.innerHTML += `
        <div class="message user-message">${userText}</div>
    `;
    input.value = "";

    // Show typing indicator
    messages.innerHTML += `
        <div class="message typing" id="typing">AI is typing...</div>
    `;
    messages.scrollTop = messages.scrollHeight;

    // Call Flask backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
    });

    const data = await response.json();

    // Remove typing indicator
    document.getElementById("typing").remove();

    // Show AI reply
    messages.innerHTML += `
        <div class="message ai-message">${data.reply}</div>
    `;
    messages.scrollTop = messages.scrollHeight;
}

// Enter key support
function handleKey(event) {
    if (event.key === "Enter") sendMessage();
}