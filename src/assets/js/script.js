// Script para animação de hover do botão
document.getElementById('clean-crow-btn').addEventListener('mouseenter', function() {
  this.style.transition = '0.3s';
  this.style.transform = 'scale(1.1)';
});

document.getElementById('clean-crow-btn').addEventListener('mouseleave', function() {
  this.style.transition = '0.3s';
  this.style.transform = 'scale(1)';
});
