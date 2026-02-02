/* Main JavaScript */

document.addEventListener('DOMContentLoaded', () => {
	// Mobile Menu Toggle
	const mobileBtn = document.querySelector('.mobile-menu-btn');
	const navLinks = document.querySelector('.nav-links');
	const navbar = document.querySelector('.navbar-wrapper');

	if (mobileBtn) {
		mobileBtn.addEventListener('click', () => {
			mobileBtn.classList.toggle('active');
			navLinks.classList.toggle('active');
		});
	}

	// Close mobile menu when a link is clicked
	document.querySelectorAll('.nav-link').forEach(link => {
		link.addEventListener('click', () => {
			mobileBtn.classList.remove('active');
			navLinks.classList.remove('active');
		});
	});

	// Sticky Navbar Effect on Scroll
	window.addEventListener('scroll', () => {
		if (window.scrollY > 50) {
			navbar.classList.add('scrolled');
		} else {
			navbar.classList.remove('scrolled');
		}
	});

	// Add simple animation to stats on intersection
	const observer = new IntersectionObserver((entries) => {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				entry.target.classList.add('animate-up');
			}
		});
	}, {
		threshold: 0.1
	});

	// Example usage for future animations
	// document.querySelectorAll('.feature-card').forEach(el => observer.observe(el));
});
