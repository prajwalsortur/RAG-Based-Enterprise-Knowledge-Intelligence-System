
import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import './App.css'
// This component provides the chat interface for the RAG application.
// It sends questions to FastAPI and displays the answers returned by the backend.
function App() {
  const [question, setQuestion] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)

  // Send a question to the existing FastAPI /ask endpoint.
  async function sendQuestion(event) {
    event.preventDefault()

    const userQuestion = question.trim()

    if (!userQuestion || loading) return

    setMessages((previous) => [
      ...previous,
      { role: 'user', text: userQuestion },
    ])

    setQuestion('')
    setLoading(true)

    try {
      const response = await fetch('http://127.0.0.1:8000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: userQuestion }),
      })

      if (!response.ok) {
        throw new Error('The server could not answer your question.')
      }

      const data = await response.json()

      setMessages((previous) => [
        ...previous,
        { role: 'assistant', text: data.answer },
      ])
    } catch (error) {
      setMessages((previous) => [
        ...previous,
        {
          role: 'assistant',
          text: `Error: ${error.message} Check that the backend is running.`,
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="app-container">
      <header className="app-header">
        <div className="app-logo">RK</div>
        <div>
          <h1>Enterprise Knowledge AI</h1>
          <p>RAG-Based Knowledge Intelligence System</p>
        </div>
      </header>

      <section className="chat-container">
        <div className="chat-heading">
          <h2>Knowledge Assistant</h2>
          <p>Ask questions about your enterprise documents.</p>
        </div>

        <div className="messages">
          {messages.length === 0 && (
            <div className="welcome-message">
              <h3>How can I help you?</h3>
              <p>
                Ask a question and I will search the available
                knowledge base for an answer.
              </p>
            </div>
          )}

          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.role}`}
            >
              <strong>
                {message.role === 'user' ? 'You' : 'Knowledge AI'}
              </strong>
              <div className="message-content">
  {message.role === 'assistant' ? (
    <ReactMarkdown>{message.text}</ReactMarkdown>
  ) : (
    <p>{message.text}</p>
  )}
</div>
            </div>
          ))}

          {loading && (
            <div className="message assistant">
              <strong>Knowledge AI</strong>
              <p>Searching the knowledge base...</p>
            </div>
          )}
        </div>

        <form className="question-form" onSubmit={sendQuestion}>
          <input
            type="text"
            value={question}
            onChange={(event) => setQuestion(event.target.value)}
            placeholder="Ask a question about your documents..."
            aria-label="Your question"
            disabled={loading}
          />

          <button type="submit" disabled={loading || !question.trim()}>
            {loading ? 'Sending...' : 'Send'}
          </button>
        </form>

        <p className="footer-note">
          Answers are generated using your connected knowledge base.
        </p>
      </section>
    </main>
  )
}

export default App
