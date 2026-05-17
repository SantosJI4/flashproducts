/** @type {import('tailwindcss').Config} */
module.exports = {
  // 1. DIRETÓRIOS DE BUSCA: Diz ao Tailwind onde procurar classes no seu projeto
  content: [
    "./templates/**/*.html",      // Todos os arquivos HTML na pasta templates (incluindo subpastas)
    "./static/js/**/*.js",        // Todos os arquivos JavaScript
    "./routes/**/*.py",           // Se você renderizar classes dinâmicas diretamente do seu backend Python
    "./app.py",
    "./main.py"
  ],
  
  theme: {
    extend: {
      // 2. CORES PERSONALIZADAS: Mantendo a identidade visual do FlashProducts
      colors: {
        kiwi: {
          DEFAULT: '#9FFF4E', // A cor verde limão/kiwi destaque da sua marca
          dark: '#86EE35',
        },
        dark: {
          DEFAULT: '#1A202C', // O tom cinza escuro/preto elegante
          surface: '#2D3748',
        },
      },
      // 3. FONTES: Caso use fontes personalizadas do Google Fonts no base.html
      fontFamily: {
        sans: ['Montserrat', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
    },
  },
  
  // 4. PLUGINS: Opcional, mas excelente para produção
  plugins: [],
}