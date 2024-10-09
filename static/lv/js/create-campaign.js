"use strict";
var KTCreateCampaign = function ()
{
	var e, a, t, n, o, i, l = [];
	return {
		init: function ()
		{
			(e = document.querySelector("#kt_modal_create_campaign")) && (new bootstrap.Modal(e), a = document.querySelector("#kt_modal_create_campaign_stepper"), t = document.querySelector("#kt_modal_create_campaign_stepper_form"), n = a.querySelector('[data-kt-stepper-action="submit"]'), o = a.querySelector('[data-kt-stepper-action="next"]'), (i = new KTStepper(a)).on("kt.stepper.changed", (function (e)
			{
				4 === i.getCurrentStepIndex() ? (n.classList.remove("d-none"), n.classList.add("d-inline-block"), o.classList.add("d-none")) : 5 === i.getCurrentStepIndex() ? (n.classList.add("d-none"), o.classList.add("d-none")) : (n.classList.remove("d-inline-block"), n.classList.remove("d-none"), o.classList.remove("d-none"))
			})), i.on("kt.stepper.next", (function (e)
			{
				console.log("stepper.next");
				var a = l[e.getCurrentStepIndex() - 1];
				a ? a.validate().then((function (a)
				{
                    //e.goNext()
					console.log("validated!"), "Valid" == a ? KTCreateCampaign.createNewGroup(e, '#kt_modal_create_campaign_stepper_form') : Swal.fire(
					{
						text: "Sorry, looks like there are some errors detected, please try again.",
						icon: "error",
						buttonsStyling: !1,
						confirmButtonText: "Ok, got it!",
						customClass:
						{
							confirmButton: "btn btn-light"
						}
					}).then((function () {}))
				})) : (e.goNext(), KTUtil.scrollTop())
			})), i.on("kt.stepper.previous", (function (e)
			{
				console.log("stepper.previous"), e.goPrevious(), KTUtil.scrollTop()
			})), n.addEventListener("click", (function (e)
			{
				e.preventDefault(), n.disabled = !0, n.setAttribute("data-kt-indicator", "on"), setTimeout((function ()
				{
					n.removeAttribute("data-kt-indicator"), n.disabled = !1, i.goNext()
				}), 2e3)
			})), function ()
			{
				var e = document.querySelector("#kt_modal_create_campaign_age_slider"),
					a = document.querySelector("#kt_modal_create_campaign_age_min"),
					n = document.querySelector("#kt_modal_create_campaign_age_max");
				noUiSlider.create(e,
				{
					start: [18, 40],
					connect: !0,
					range:
					{
						min: 13,
						max: 80
					}
				}), e.noUiSlider.on("update", (function (e, t)
				{
					t ? n.innerHTML = Math.round(e[t]) : a.innerHTML = Math.round(e[t])
				}));

				new Dropzone("#kt_modal_create_campaign_files_upload",
				{
					url: "https://keenthemes.com/scripts/void.php",
					paramName: "file",
					maxFiles: 10,
					maxFilesize: 10,
					addRemoveLinks: !0,
					accept: function (e, a)
					{
						"wow.jpg" == e.name ? a("Naha, you don't.") : a()
					}
				});
				const r = document.querySelector("#kt_modal_create_campaign_duration_all"),
					c = document.querySelector("#kt_modal_create_campaign_duration_fixed"),
					s = document.querySelector("#kt_modal_create_campaign_datepicker");
				[r, c].forEach((e =>
				{
					e.addEventListener("click", (a =>
					{
						e.classList.contains("active") || (r.classList.toggle("active"), c.classList.toggle("active"), c.classList.contains("active") ? s.nextElementSibling.classList.remove("d-none") : s.nextElementSibling.classList.add("d-none"))
					}))
				}));
				var d = document.querySelector("#kt_modal_create_campaign_budget_slider"),
					u = document.querySelector("#kt_modal_create_campaign_budget_label");
				noUiSlider.create(d,
				{
					start: [5],
					connect: !0,
					range:
					{
						min: 1,
						max: 500
					}
				}), d.noUiSlider.on("update", (function (e, a)
				{
					u.innerHTML = Math.round(e[a]), a && (u.innerHTML = Math.round(e[a]))
				})), document.querySelector("#kt_modal_create_campaign_create_new").addEventListener("click", (function ()
				{
					t.reset(), i.goTo(1)
				}))
			}(), l.push(FormValidation.formValidation(t,
			{
				fields:
				{
					group_title:
					{
						validators:
						{
							notEmpty:
							{
								message: "Group title is required"
							}
						}
					},
					avatar:
					{
						validators:
						{
							file:
							{
								extension: "png,jpg,jpeg",
								type: "image/jpeg,image/png",
								message: "Please choose a png, jpg or jpeg files only"
							}
						}
					}
				},
				plugins:
				{
					trigger: new FormValidation.plugins.Trigger,
					bootstrap: new FormValidation.plugins.Bootstrap5(
					{
						rowSelector: ".fv-row",
						eleInvalidClass: "",
						eleValidClass: ""
					})
				}
			})))
		},
        createNewGroup : function(e, kt_modal_create_campaign_stepper_form) {
            e.goNext()
            var formData = KTCreateCampaign.serializeFormData(kt_modal_create_campaign_stepper_form);
            console.log(kt_modal_create_campaign_stepper_form);
            var settings = {
                "url": "http://18.190.86.79:5081/graphiql",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1YmM2MzY0OTg5Nzk5NTc0NmQyOWEyYTIiLCJqdGkiOiJiM2YyNjQ0MGViZDk3NjFlMzJmNWZjZjBjMjhjYTk3MTcyZTc1Y2FjODUwYTM3ODU4MTBjNDFkOTJjMTc5Mzc4OTQ4YmM1YjI5NmRjOGI2YiIsImlhdCI6MTY0MTg5MjMwOSwibmJmIjoxNjQxODkyMzA5LCJleHAiOjE2NzM0MjgzMDksInN1YiI6IjVmZGM3ZGFhMTE3OTdjMjFiYjVhYmNjMiIsInNjb3BlcyI6W119.PsHVAMtxD-D0xpXgb9pz_Mm0b7xtsafnhlY9azzK-1DYTmx9KKdEjgQVGa-1HAbS___CNUjAP0uvtVffrksb52eaWP-H0nOxQ4UhUpBaq7WOHpjZijRvsJsuwj8vqkMtKYp6Ewk8IZj1cZXPtHCYx_KYG63BOomhkOr_T01TgUtd9KIkhbToVJIac7fAgJLq0wfFU6bStX4qN0scXm8EuQ4YAN24Oce94dj2gZsDWmawcGEbHzFfHvEPOsgIcIRxR8uTpGRhKzDYikxCh87tD4T0OStiDvn11FKHATITQ6BPc3sv9Irulr9yFL9TLjZEBPTVmF9lW7QXmIcOXWg07EP9JR3TqSCwv5ycQuO4gYD4-tpL34iZaJ0K0miLK1KHiZ-5NHVJAM41L9tgcbcFLx4RqwM-xBjiHnHHikFun05wwQjapyjI6U0hFEsdp0a9PTT-ec8nyy1ujRFlBrn6mXx_CU0YOu65Gg-JFDsK4lS24Zz3RuXQP_ZGsrhU6a9Y2-evb1GftEb3KVRqrvfa_AcNhf6yVVK2h-dQRBDvMYYgBcwHA1nh1JIrbo1_z6Z6Bk3JjO2NDB59KPHY-1u1cBvtiZkjQzJVbmIH8UI6SkDkZZlV46RqZX46nYyWwf1ir2yphMQv_n0YbfzMUWbsj-Nc5-50kM7X791fQV_pzqg",
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify({
                    query: `mutation{
                      createGroup(categoryId:`+formData.group_category+`,createdBy:"admin",description:"`+formData.details_description+`", featuredImage:"", name:"`+formData.group_title+`", userId:"925d6504-6657-4d5c-bd26-e2154de0184d", visibility:"`+formData.group_privacy+`")
                      {
                        id
                      }
                    }`,
                    variables: {}
                })
              };
            $.ajax(settings).done(function (response) {
                if(response.errors) {
                    Swal.fire(
                    {
                        text: response.errors[0].message,
                        icon: "error",
                        buttonsStyling: !1,
                        confirmButtonText: "Ok, got it!",
                        customClass:
                        {
                            confirmButton: "btn btn-light"
                        }
                    }).then((function () {}))
                }
                else {
                    e.goNext()
                }
                console.log(response);
            });
        },
        serializeFormData : function (kt_modal_create_campaign_stepper_form) {
            var o = {};
            var a = jQuery(kt_modal_create_campaign_stepper_form).serializeArray();
            $.each(a, function () {
                if (o[this.name]) {
                    if (!o[this.name].push) {
                        o[this.name] = [o[this.name]];
                    }
                    o[this.name].push(this.value || '');
                } else {
                    o[this.name] = this.value || '';
                }
            });
            return o;
        },
        fetchCategories : function() {
            var settings = {
                "url": "http://18.190.86.79:5081/graphiql",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1YmM2MzY0OTg5Nzk5NTc0NmQyOWEyYTIiLCJqdGkiOiJiM2YyNjQ0MGViZDk3NjFlMzJmNWZjZjBjMjhjYTk3MTcyZTc1Y2FjODUwYTM3ODU4MTBjNDFkOTJjMTc5Mzc4OTQ4YmM1YjI5NmRjOGI2YiIsImlhdCI6MTY0MTg5MjMwOSwibmJmIjoxNjQxODkyMzA5LCJleHAiOjE2NzM0MjgzMDksInN1YiI6IjVmZGM3ZGFhMTE3OTdjMjFiYjVhYmNjMiIsInNjb3BlcyI6W119.PsHVAMtxD-D0xpXgb9pz_Mm0b7xtsafnhlY9azzK-1DYTmx9KKdEjgQVGa-1HAbS___CNUjAP0uvtVffrksb52eaWP-H0nOxQ4UhUpBaq7WOHpjZijRvsJsuwj8vqkMtKYp6Ewk8IZj1cZXPtHCYx_KYG63BOomhkOr_T01TgUtd9KIkhbToVJIac7fAgJLq0wfFU6bStX4qN0scXm8EuQ4YAN24Oce94dj2gZsDWmawcGEbHzFfHvEPOsgIcIRxR8uTpGRhKzDYikxCh87tD4T0OStiDvn11FKHATITQ6BPc3sv9Irulr9yFL9TLjZEBPTVmF9lW7QXmIcOXWg07EP9JR3TqSCwv5ycQuO4gYD4-tpL34iZaJ0K0miLK1KHiZ-5NHVJAM41L9tgcbcFLx4RqwM-xBjiHnHHikFun05wwQjapyjI6U0hFEsdp0a9PTT-ec8nyy1ujRFlBrn6mXx_CU0YOu65Gg-JFDsK4lS24Zz3RuXQP_ZGsrhU6a9Y2-evb1GftEb3KVRqrvfa_AcNhf6yVVK2h-dQRBDvMYYgBcwHA1nh1JIrbo1_z6Z6Bk3JjO2NDB59KPHY-1u1cBvtiZkjQzJVbmIH8UI6SkDkZZlV46RqZX46nYyWwf1ir2yphMQv_n0YbfzMUWbsj-Nc5-50kM7X791fQV_pzqg",
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify({
                  query: "{\n  categories(pageNo:1, perPage:10){\n    list{\n      id\n      name\n    }\n  }\n}",
                  variables: {}
                })
              };

              $.ajax(settings).done(function (response) {
                console.log(response);
                return response
              });
        }
	}
}();
KTUtil.onDOMContentLoaded((function ()
{
	KTCreateCampaign.init()
}));
