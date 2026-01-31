(function(){
	function qs(sel){return document.querySelector(sel)}
	function qsa(sel){return Array.from(document.querySelectorAll(sel))}

	function ensureToastContainer(){
		let c = qs('.toast-container')
		if(!c){ c = document.createElement('div'); c.className='toast-container'; document.body.appendChild(c) }
		return c
	}

	function showToast(message, type='info', ttl=3200){
		const c = ensureToastContainer()
		const t = document.createElement('div')
		t.className = `toast ${type}`
		t.textContent = message
		c.appendChild(t)
		
		requestAnimationFrame(()=> t.classList.add('show'))
		setTimeout(()=>{ t.classList.remove('show'); setTimeout(()=> t.remove(),220) }, ttl)
	}

	function applyTheme(theme){
		document.body.classList.toggle('theme-light', theme === 'light')
		try{ localStorage.setItem('quiz:theme', theme) }catch(e){}
	}
	function initTheme(){
		const saved = (localStorage.getItem('quiz:theme')) || (window.matchMedia && window.matchMedia('(prefers-color-scheme:light)').matches ? 'light' : 'dark')
		applyTheme(saved)
		const btn = qs('#theme-toggle')
		if(btn) btn.addEventListener('click', ()=> applyTheme(document.body.classList.contains('theme-light') ? 'dark' : 'light'))
	}

	// Hamburger nav
	function initHamburger(){
		const burger = qs('.hamburger')
		const nav = qs('.nav-links')
		if(!burger || !nav) return
		burger.addEventListener('click', ()=> nav.classList.toggle('mobile-active'))
	}

	// Quiz options handling: expects .option elements with data-correct="true" on correct answers
	function initOptions(){
		const options = qsa('.option')
		if(!options.length) return
		options.forEach(opt=>{
			opt.addEventListener('click', ()=>{
				if(opt.classList.contains('disabled')) return
				// mark selected
				options.forEach(o=>o.classList.remove('selected'))
				opt.classList.add('selected')
				// reveal correct/wrong
				const correct = opt.dataset.correct === 'true' || opt.getAttribute('data-correct') === 'true'
				options.forEach(o=>{
					o.classList.add('disabled')
					const isCorrect = o.dataset.correct === 'true' || o.getAttribute('data-correct') === 'true'
					if(isCorrect) o.classList.add('correct')
				})
				if(correct){
					opt.classList.add('correct')
					showToast('Nice — correct!', 'success', 2000)
				} else {
					opt.classList.add('wrong')
					showToast('Oops — that was incorrect', 'error', 3000)
				}
			})
		})
	}

	// Reveal animations for elements with .reveal
	function initReveal(){
		const els = qsa('.reveal')
		if(!els.length) return
		els.forEach((el,i)=> setTimeout(()=> el.classList.add('visible'), 80*i))
	}

	// init on DOM ready
	document.addEventListener('DOMContentLoaded', ()=>{
		initTheme(); initHamburger(); initOptions(); initReveal()
		// Expose a global toast helper
		window.showToast = showToast
	})

})()

